# HOL practice

from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!\n"

# Returning json with python dict
@app.route('/hijson1')
def index_1():
    return { "message": "Hello everyone!!" } 

# returning json with jsonify()
@app.route('/hijson2')
def index_2():
    return jsonify( message="Hello i was a string, but jsonify() helped me become JSON string")
