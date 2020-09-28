# coding=utf-8

from flask import Blueprint

app1 = Blueprint('hello', __name__)

@app1.route('/')
def index(name):
    return 'Hello,World!'
