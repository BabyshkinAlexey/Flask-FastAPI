from models import db, Author, Book
from flask import Flask, render_template
from random import choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Все таблицы созданы успешно!')
    

@app.cli.command("add-books")
def fill_tables():
    count = 5
    for author in range(count):
        new_author = Author(name=f'Author{author}', surname=f'Surname{author}')
        db.session.add(new_author)
    db.session.commit()
    # Добавляем книги
    for book in range(1, count ** 2):
        author = choice(range(1, count+1))
        new_book = Book(title=f'Title{book}', year=choice(range(1900, 2020)),author=author)
        db.session.add(new_book)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)