from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clientlist_database import Base, Tenant, Room

app = Flask(__name__)

engine = create_engine('sqlite:///clientlist_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/')
@app.route('/tenants/')
def showTenants():
    tenants = session.query(Tenant).all()
    return render_template('list.html', f_name = f_name,l_name = l_name, email = email)


# def showTenants(f_name = 'Kennedy', l_name = 'DeSousa', email = 'email' ):
#     return render_template('list.html', f_name = f_name,l_name = l_name, email = email)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(debug = True, host = '0.0.0.0', port = 5555)
