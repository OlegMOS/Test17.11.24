from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    user_data = {}
    if request.method == 'POST':
        user_data['name'] = request.form.get('name')
        user_data['city'] = request.form.get('city')
        user_data['hobby'] = request.form.get('hobby')
        user_data['age'] = request.form.get('age')

    return render_template('form.html', user_data=user_data)


if __name__ == '__main__':
    app.run()