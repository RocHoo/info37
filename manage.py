from flask import Flask,session

from flask_session import Session

from redis import StrictRedis

from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand

app=Flask(__name__)

app.config['SECRET_KEY']='dxdvvrEG3IvY8kz1FyE7rYOZexjl+IsiSD8EBo8J7iEMwQ4pLuY8pg=='

app.config['SESSION_TYPE']='redis'

app.config['SESSION_REDIS']=StrictRedis(host='127.0.0.1',port=6379)

app.config['SESSION_USE_SIGNER']=True

app.config['PERMANENT_SESSION_LIFETIME']=86400

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql@localhost/info_python37'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

Session(app)

db=SQLAlchemy(app)

manage=Manager(app)

Migrate(app,db)

manage.add_command('db',MigrateCommand)

@app.route('/')
def index():
    session['itcast']='2019'
    return 'hello world2018'


if __name__ == '__main__':
    manage.run()