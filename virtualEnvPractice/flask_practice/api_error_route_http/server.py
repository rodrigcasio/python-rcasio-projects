# HOL practice 2
from flask import Flask, jsonify, make_response, request
from data_people import data
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
            return ({ "message": f"Data length {len(data)} found"}, 200)
        else:
            return ({ "message": "Data is empty" }, 500)

    except NameError:
        return ({ "message": "Data not found" }, 404)


@app.route('/name_search')
def name_search():
    query = request.args.get("q")
    
    if query is None:
        return ({ "message": "Query parameter 'q' is missing. Please try again" }, 400)
    
    if query.strip() == "" or query.isdigit():
        return ({ "message": "Invalid input parameter" }, 422)
    
    for person in data:
        if query.lower() == person["first_name"].lower():
            return person, 200
    
    return ({ "message": "Person not found" }, 404)


"""
First approach for '/name_search'

@app.route('/name_search')
def name_search():
    first_name = request.args['q']
    
    if first_name:
        person = find_person(first_name)
        if person["first_name"] == first_name:
            return (jsonify(person), 200)
        else:
            return ( {"message": "Person not found"}, 404)
    else:
        return ( { "message": "Invalid input parameter"}, 400)
"""
