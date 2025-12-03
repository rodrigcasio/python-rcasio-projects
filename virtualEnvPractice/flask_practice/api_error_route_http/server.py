# HOL practice 2
# " # exercise"
from flask import Flask, jsonify, make_response, request
from data_people import find_person, data
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

# "1 setup no response status code:"
@app.route('/no_content')
def no_content():
    return ({ "message": "No content found" }, 204) # string is not returned with 204

@app.route('/exp')
def index_explicit():
    res = make_response( { "message": "Hello World! 'make_response()' used" } )
    res.status_code = 200
    
    return res

# "2 Process input arguments"
@app.route('/data')
def get_data():
    try:
        if data and len(data) > 0:
            return ({ "People": data }, 200)
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

    found_person = find_person(query)
    if query.lower() == found_person["first_name"].lower():
        return found_person, 200
    """
    for person in data:
        if query.lower() == person["first_name"].lower():
            return person, 200
    """
    return ({ "message": "Person not found" }, 404)

# 'Add Dynamic URLs'
@app.route('/count')
def count():
    try:
        return ({ "data count": f"{len(data)}"}, 200)
     
    except NameError:
        return ({ "message": "data is not defined" }, 500)


@app.route('/person/<uuid:id>')
def find_by_uuid(id):
    for person in data:
        if str(id) == person["id"]:
            return person, 200
   
    return ({ "message": "Person not found" }, 404)  
 

@app.route('/person/<uuid:id>', methods = ['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if str(id) == person["id"]:
            data.remove(person)
            return ({ "message": f"Person with ID {id} deleted successfully"}, 200)   

    return ({ "message": "Person not found" }, 404)

# "4 Parse JSON from Request body"
@app.route('/person', methods = ['POST'])
def create_new_person():
   new_person = request.json
   
   if not new_person:
       return ({ "message": "Invalid input parameter" }, 422)

   if new_person in data:
       return ({ "message": "Person already created, and saved" }, 403)
   
    # validate new_person 
   try:
       data.append(new_person)
   except NameError:
       return ({ "message": "Data not defined" }, 500)

   return ({ "ID": new_person["id"], "messsage": "Person created successfully"}, 200)
 
# "5 Add Error handlers"   

@app.route("/test500")
def test500():
    """
    Deliberately raise an exception to test the global handler "handle_exception(e)"
    curl -i localhost:5000/test500
    Placing purposely this route before the error handlers
    """
    raise Exception("Forced exception for testing!")

@app.errorhandler(404)
def api_not_found(err):
    """
    function triggers whenever a client requests a URL that does not lead to any endpoints defined by server:
    curl -X POST -i -w localhost:5000/notvalid
    """
    if err:
       return ({ "message": "API not found"}, 404)

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Catch any unhandled Exception raised anywhere in the app and route
    to this handler
    """
    return ({ "message": str(e) }, 500)



"""
First approach for '/name_search' making use data directly:

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

to test create_new_person POST method:
curl -X POST -i -w '\n' --url http://localhost:5000/person --header 'Content-Type: application/json' --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'
"""
