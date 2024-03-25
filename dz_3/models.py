from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    
    author = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return f'Book ({self.title})'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    
    books = db.relationship('Book', backref='author_name', lazy=True)

    def __repr__(self):
        return f'Author ({self.name} {self.surname})'