from flask import Flask

# creating instance of the Flask class and naming it "Hello World App"
app = Flask("My Hello World App")


# Define route for the root URL (/)
@app.route("/")
def hello():
    return "Hello everyone!, and world lol"


# Checking if this script is being run directly (meaning, not imported as a module)
if __name__ == "__main__":
    app.run(debug=True)  # start the flask development server WITH debugging enabled

    # , and when no port is specified, the server starts at the default port 5000
