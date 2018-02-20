from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
#Below added a route to f_name.
@app.route('/<string:f_name>')
#When you can re-define the route which that defines the f_name and the l_name
def hello(f_name = 'Kennedy',l_name = 'DeSousa'):
    return render_template('list.html', f_name = f_name,l_name = l_name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return '{} + {} = {}'.format(num1,num2,num1+num2)




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5005)
