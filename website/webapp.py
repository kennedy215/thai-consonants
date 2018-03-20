from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Tenant, Room


app = Flask(__name__)


engine = create_engine('sqlite:///website.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/user/')
def user():
    return render_template('user.html')

@app.route('/contact/', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
    return render_template('contact.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5055)
