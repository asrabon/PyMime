import json
import requests

from ._auth import set_access_token

# Mimecast URL Definitions
GET_PROFILE_GROUPS_URL = "https://api.services.mimecast.com/api/directory/find-groups"
GET_GROUP_MEMBERS_URL = "https://api.services.mimecast.com/api/directory/get-group-members"

@set_access_token
def get_profile_groups(self):
    r = requests.post(
        GET_PROFILE_GROUPS_URL,
        headers={
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "meta": {
                "pagination": {
                    "pageSize": 500
                }
            }
        })
    )
    return json.loads(r.content)

@set_access_token
def get_group_members(self, id):
    r = requests.post(
        GET_GROUP_MEMBERS_URL,
        headers={
            "Authorization": f"Bearer {self.access_token}",
        },
        data = json.dumps({
            "meta": {
                "pagination": {
                    "pageSize": 999
                }
            },
            "data": [
                {
                    "id": id
                }
            ]
        })
    )

    return json.loads(r.content)
