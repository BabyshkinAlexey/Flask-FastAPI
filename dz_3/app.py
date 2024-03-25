from models import db, Author, Book
from flask import Flask, render_template
from random import choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

category = [
    {"title": 'All books', "func_name": 'get_all_books'},
]


@app.route('/')

@app.route('/index/')
def index():
    return render_template('index.html', category=category)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Все таблицы созданы успешно!')
    

@app.cli.command("fill-books")
def fill_tables():
    count = 5
    for author in range(count):
        new_author = Author(name=f'Author{author}', surname=f'Surname{author}')
        db.session.add(new_author)
    db.session.commit()
    for book in range(1, count ** 2):
        author = choice(range(1, count+1))
        new_book = Book(title=f'Title{book}', year=choice(range(1900, 2020)),author=author)
        db.session.add(new_book)
    db.session.commit()
    
@app.route('/all_books/')
def get_all_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('all_books.html', **context)

if __name__ == '__main__':
    app.run(debug=True)