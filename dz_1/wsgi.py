from flask import Flask
from flask import render_template
app = Flask(__name__)

html = """
<h1> Магазин одежды </h1>
<p> Одежда </p>
<p> Обувь </p>
<p> Куртки </p>
"""

_clothes = [{'name': 'Майка','color': 'белая','price': '100р.'},
            {'name': 'Носки','color': 'черные','price': '70р.'},
            {'name': 'Футболка','color': 'серая','price': '140р.'}]

_jacket = [{'name': 'Бомбер','color': 'белый','price': '2000р.'},
            {'name': 'Пуховик','color': 'серый','price': '3000р.'},
            {'name': 'Ветровка','color': 'синяя','price': '1500р.'}]

_footwear = [{'name': 'Кроссовки','color': 'красные','price': '800р.'},
            {'name': 'Ботинки','color': 'черные','price': '1500р.'},
            {'name': 'Берцы','color': 'черные','price': '3000р.'}]

@app.route("/")
def web():
    return html

@app.route("/clothes/")
def clothes():
    return render_template("clothes.html", content = _clothes)

@app.route("/footwear/")
def footwear():
    return render_template("footwear.html", content = _footwear)

@app.route("/jacket/")
def jacket():
    return render_template("jacket.html", content = _jacket)

if __name__ == '__main__':
    app.run(debug=True)