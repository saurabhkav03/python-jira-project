# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

#Specifies the endpoint URL of the Jira API that returns information about projects.
url = "https://kaverisaurabh1998.atlassian.net//rest/api/3/project"

api_token = os.getenv("API_TOKEN")

auth = HTTPBasicAuth("kaverisaurabh1998@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#response.text is used to access the raw JSON response content, and json.loads() is used to parse this content into a Python data structure.
structure = json.loads(response.text)
for i in range(len(structure)):
    project_name = structure[0]["name"]
    print(project_name)