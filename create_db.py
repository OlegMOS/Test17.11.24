from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from app.models import User

with app.app_context():  # Создаём контекст приложения
    db.create_all()  # Создаёт базы данных и таблицы