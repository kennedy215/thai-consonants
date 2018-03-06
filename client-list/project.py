from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
# Below added a route to f_name.
@app.route('/clients/<int:client_id>/room')
#When you can re-define the route which that defines the f_name and the l_name
def clientList(client_id):
    clients = session.query(Client).filter_by(id=client_id).one()




#
# def hello(f_name = 'Kennedy',l_name = 'DeSousa'):
#     return render_template('list.html', f_name = f_name,l_name = l_name)

# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1,num2):
#     return '{} + {} = {}'.format(num1,num2,num1+num2)
#
# @app.route('/<name>')
# def default(name = "default"):
#     return 'Hello default  {}'.format(name)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5555)
