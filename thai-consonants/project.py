from flask import Flask, render_template, session
from flask import render_template
from sqlalchemy.orm import sessionmaker
from database_list import Base, lowConsonants

# One way of connecting css file
# app = Flask(__name__,static_url_path='/css')
app = Flask(__name__)


@app.route('/')
# @app.route('/<string:name>')
# @app.route('/low')
# def hello(name=None):
def hello():
    # low_consonants = session.query(lowConsonants).all()
    # if name == None:
        # returns message
        # return '{} You Must Input Name'.format('User')
        # returns redefined variable name
        # name = 'New User'
    # return render_template('low.html', low=low)
    return render_template('index.html')
    # else:
    #     return render_template('low.html', name=name)

# @app.route('/consonants/<string:low>/new', methods=['GET','POST'])
# def low(name=low):
#     return render_template('index.html',name=low)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5050)
