from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world with Flask'

@app.route('/hello')
def hello1():
    return 'Hello world with Flask'
