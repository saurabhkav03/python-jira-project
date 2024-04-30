##################################
##
## Author: Saurabh Kaveri
## Date: 30-04-2024
##
## Description: 
##   This is a very simple Flask API. When someone hits this Flask API on the internet with a GET request, 
##   they will receive a response of "Hello World".
##
## Version: v1
##
##################################

# from the flask package import the flask module to keep it light
from flask import Flask

# creating a Flask application instance (Flask framework)
app = Flask(__name__)

# decorator: In Flask, this particular decorator verifies if someone is trying to access the / path. 
# If so, Flask will send the request to the hello function.
@app.route("/")

# Main function
def hello():
    return "Hello World"

# Run the application on the EC2 instance IP.
app.run("0.0.0.0")
