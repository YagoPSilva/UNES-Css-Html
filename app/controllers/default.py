from unicodedata import name
from flask import render_template
from app import app


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')
