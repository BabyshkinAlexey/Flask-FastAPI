from flask import Flask
from flask import render_template
app = Flask(__name__)

html = """
<h1> Моя первая html страница </h1>
<p> Привет мир! </p>

"""

_users = [{'name': 'Ivan','Last_name': 'Ivanov','age': '44','average_mark': '4.8',},
          {'name': 'Ivan','Last_name': 'Ivanov','age': '44','average_mark': '4.8',} ]

_news = [{'title': 'MAIN_news','content': 'sdsdg','date': '2024-02-04',},
         {'title': 'other_news','content':'fgsfg','date': '2024-02-05',},]

@app.route("/")
def web():
    return html

@app.route("/table/")
def table():
    return render_template("table.html", users = _users)

@app.route("/about/")
def about_html():
    return "about.html"

@app.route("/contacts/")
def contacts_html():
    return "contacts.html"

@app.route("/number/<int:num1>/<int:num2>/")
def sum(num1, num2):
    return str(num1 + num2)

@app.route("/lenght/<text>/")
def text_lenght(text):
    return str(len(text))

@app.route("/news/")
def news():
    return render_template("news.html", news = _news)

if __name__ == '__main__':
    app.run(debug=True)