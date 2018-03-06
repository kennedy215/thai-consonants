# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from the name of the model import the Base and Class
from database_list import Base, lowConsonants

# One way of connecting css file
# app = Flask(__name__,static_url_path='/css')
app = Flask(__name__)

engine = create_engine('sqlite:///thaiconsonants.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newLowConsonants():
    if request.method == 'POST':
        newLowConsonants = lowConsonants(name=request.form['name'])
        session.add(newLowConsonants)
        session.commit()
        return redirect(url_for('form.html'))
    else:
        return render_template('form.html')




        # returns message
        # return '{} You Must Input Name'.format('ก')
        # returns redefined variable name
        # name = 'New User'
        # return render_template('index.html', name=name)
    # else:
    #     return render_template('form.html', name=name)

# @app.route('/consonants/<string:low>/new', methods=['GET','POST'])
# def low(name=low):
#     return render_template('index.html',name=low)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5555)
