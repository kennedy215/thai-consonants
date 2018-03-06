from flask import Flask
from flask import render_template

# One way of connecting css file
# app = Flask(__name__,static_url_path='/css')
app = Flask(__name__)


@app.route('/')
@app.route('/<string:name>')
def hello(name=None):
    if name == None:
        # returns message
        # return '{} You Must Input Name'.format('User')
        # returns redefined variable name
        name = 'New User'
        return render_template('index.html', name=name)
    else:
        return render_template('index.html', name=name)

# @app.route('/consonants/<string:low>/new', methods=['GET','POST'])
# def low(name=low):
#     return render_template('index.html',name=low)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5050)
