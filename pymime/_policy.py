from ._auth import set_access_token

# Mimecast URL Defintions 
GET_POLICY_URL = "https://api.services.mimecast.com/api/policy/blockedsenders/get-policy"

@set_access_token
def get_policies(self):
    return self.make_mimecast_request(GET_POLICY_URL)
