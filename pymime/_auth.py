from datetime import datetime, timedelta
import json
import requests

# Define Mimecast API Endpoints
OAUTH_URL = "https://api.services.mimecast.com/oauth/token"

def get_access_token(self):
    r = requests.post(
        OAUTH_URL,
        data={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
    )

    token_json = json.loads(r.content)
    if "access_token" in token_json:
        return token_json["access_token"]
    else:
        raise Exception(f"An error occurred while getting your access token please see the JSON output from Mimecast: {token_json}")
    
# Decorator to require an access token
def set_access_token(func):
    """
    Decorator to ensure access token is available before calling a function.

    Args:
        func (function): Function to decorate
    """
    def wrapper(self, *args, **kwargs):
        # Check if we have an access token or if it has expired
        if self.access_token is None or self.expiration < datetime.now():
            self.access_token = self.get_access_token()
            self.expiration = datetime.now() + timedelta(seconds=1500)

        return func(self, *args, **kwargs)
    return wrapper