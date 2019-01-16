from flask import Flask,session

from flask_session import Session

from redis import StrictRedis

app=Flask(__name__)

app.config['SECRET_KEY']='dxdvvrEG3IvY8kz1FyE7rYOZexjl+IsiSD8EBo8J7iEMwQ4pLuY8pg=='

app.config['SESSION_TYPE']='redis'

app.config['SESSION_REDIS']=StrictRedis(host='127.0.0.1',port=6379)

app.config['SESSION_USE_SIGNER']=True

app.config['PERMANENT_SESSION_LIFETIME']=86400

Session(app)


@app.route('/')
def index():
    session['itcast']='2019'
    return 'hello world2018'


if __name__ == '__main__':
    app.run(debug=True)