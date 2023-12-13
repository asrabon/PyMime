# Standard Python modules
import json
import requests

# Local Python modules
from ._auth import set_access_token

@set_access_token
def make_mimecast_request(self, url, data=None):
    headers = {
        "Authorization": f"Bearer {self.access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "meta": {
            "pagination": {
                "pageSize": 999
            }
        },
    }
    if data is not None:
        print(type(data))
        print(data)
        payload["data"] = data
    print(payload)
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return json.loads(response.content)