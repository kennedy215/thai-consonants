from flask import Flask
from flask import render_template

# One way of connecting css file
# app = Flask(__name__,static_url_path='/css')
app = Flask(__name__)


@app.route('/')
@app.route('/<string:name>')
def hello(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5050)
