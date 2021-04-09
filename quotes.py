from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

import os
print(os.environ['HOME'])

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:psVon8bis5.@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://aizfvhpocexyci:f82281d2cfd575b53b72e2f55c9efe8a06960b14002d0a61baaf2224d3eeebae@ec2-54-74-14-109.eu-west-1.compute.amazonaws.com:5432/d8vcedu86jf1os'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result,welcome='moin moin')

@app.route('/about')
def about():
    fruits = ["apple","orange","berries"]
    return render_template('about.html',fruits=fruits)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
