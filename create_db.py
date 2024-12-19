from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Замените на свою строку подключения
db = SQLAlchemy(app)

# Определение моделей здесь...

if __name__ == "__main__":
    with app.app_context():  # Создаём контекст приложения
        db.create_all()  # Создаёт базы данных и таблицы