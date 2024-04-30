# Import necessary modules
from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os 

# Create a Flask application instance
app = Flask(__name__)

# Define endpoint and allowed methods
@app.route("/createJira", methods=['POST'])
def createJira():
    # Define Jira API endpoint
    url = "https://kaverisaurabh1998.atlassian.net/rest/api/3/issue"
    
    # Get authentication token from environment variable
    auth_token = os.getenv("AUTH_TOKEN")
    
    # Create authentication object
    auth = HTTPBasicAuth("kaverisaurabh1998@gmail.com", auth_token)
    
    # Define request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Define payload for creating Jira issue
    payload = json.dumps({
        "fields": {
            "issuetype": {"id": "10001"},
            "project": {"key": "SCRUM"},
            "summary": "Create my first issue using API"
        }
    })
    
    # Check if request contains '/jira' in the comment body
    if request.json.get("comment", {}).get("body") == "/jira":
        # Make a POST request to create Jira issue
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        # Return JSON response from Jira API
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # Return message if '/jira' is not found in the comment body
        return "Not Found !!!!!! \n Please enter the correct URL"


# Run the application on the specified IP and port
app.run("0.0.0.0", port=6000)
