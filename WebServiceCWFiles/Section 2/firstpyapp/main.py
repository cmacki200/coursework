import flask

#App engine will automatically look for 'app' within main.py unless specified in the config file
app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def myname():
    "We return the student's name"
    return "Hello, my name is chris\n"
#Function which simply returns a message with the student name