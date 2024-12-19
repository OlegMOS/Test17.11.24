from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)  # Исправлено на __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

class UserForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Создать профиль')

class EditUserForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Новый пароль (оставьте пустым, если не хотите менять)')
    submit = SubmitField('Сохранить изменения')

@app.route('/create', methods=['GET', 'POST'])
def create_profile():
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Профиль создан!', 'success')
        return redirect(url_for('edit_profile', user_id=new_user.id))
    return render_template('create.html', form=form)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])  # Исправлено на <int:user_id>
def edit_profile(user_id):
    user = User.query.get_or_404(user_id)
    form = EditUserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        if form.password.data:  # Если пароль введён, обновляем его
            user.password = generate_password_hash(form.password.data, method='sha256')
        db.session.commit()
        flash('Профиль обновлён!', 'success')
        return redirect(url_for('edit_profile', user_id=user.id))
    return render_template('edit.html', form=form, user=user)

if __name__ == '__main__':  # Исправлено на __name__ и __main__
    app.run(debug=True)  # Рекомендуется использовать debug=True для отладки