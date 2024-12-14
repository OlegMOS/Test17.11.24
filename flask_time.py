from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Получаем текущее время
    now = datetime.now()
    # Форматируем дату и время
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return f"<h1>Текущая дата и время: {current_time}</h1>"

if __name__ == '__main__':
    app.run()