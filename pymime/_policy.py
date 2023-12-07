import json
import requests

from ._auth import set_access_token

# Mimecast URL Defintions 
GET_POLICY_URL = "https://api.services.mimecast.com/api/policy/blockedsenders/get-policy"

@set_access_token
def get_policies(self):
    r = requests.post(
        GET_POLICY_URL,
        headers={
            "Authorization": f"Bearer {self.access_token}",
        }
    )

    return json.loads(r.content)
