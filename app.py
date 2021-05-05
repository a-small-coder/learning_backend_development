from flask import Flask, render_template, url_for
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/product')
def product():
    return render_template("product.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")


@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


if __name__ == "__main__":

    app.run(debug=True)
