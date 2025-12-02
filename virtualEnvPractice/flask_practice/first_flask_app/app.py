# first flask app
from flask import Flask 
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b> My first Flask app in actionnnn </b>"

# Returning JSON example
@app.route('/hijson')
def index():
    return { "message": "Hello everyone!" }

@app.route('/hijson2')
def index_2():
    return jsonify(message="Hello, i just used `jsonify()` for this message")


"""
To run flask in terminal:
export FLASK_APP=app.pya
export FLASK_ENV=developement
flask run 

Running flask with automatic reset of server after changes made
flask --app app.py --debug run
(kinda like deamon module in node.js)

can use:
curl -X GET -i localhost:5000
to obtain within the terminal, the response from the server

-i : tells curl to include the HTTP response headers in the output
"""
