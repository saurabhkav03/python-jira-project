# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os 

url = "https://kaverisaurabh1998.atlassian.net//rest/api/3/issue"

auth_token = os.getenv("AUTH_TOKEN")

auth = HTTPBasicAuth("kaverisaurabh1998@gmail.com", auth_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "Create my first issue using API"
  }
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
