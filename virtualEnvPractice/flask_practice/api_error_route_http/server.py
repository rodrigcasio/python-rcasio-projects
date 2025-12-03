# HOL practice 2
from flask import Flask, jsonify, make_response, request
from data import data
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/hijson1')
def greet():
    return { "message": "Hello Everyone! I turned into a JSON string form dict. " }

@app.route('/hijson2')
def greet_2():
    return jsonify( message = "Hello everyone, i turned into a JSON string with 'jsonify()' " )

# 1
# setting response status:
# import make_response
@app.route('/no_content')
def no_content():
    return ({ "message": "No content found" }, 204) # string is not returned with 204

@app.route('/exp')
def index_explicit():
    res = make_response( { "message": "Hello World! 'make_response()' used" } )
    res.status_code = 200
    
    return res
# 2
# confirming if data exists
@app.route('/data')
def get_data():
    try:
        if data and len(data) > 0:
            return { "message": f"Data length {len(data)} found"}
        else:
            return { "message": "Data is empty" }, 500

    except NameError:
        return { "message": "Data not found" }, 404



