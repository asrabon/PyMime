from datetime import datetime

class PyMime(object):
    # Imported methods
    from ._auth import get_access_token
    from ._directory import get_group_members, get_profile_groups
    from ._policy import get_policies
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.expiration = datetime.now()
        
        self.access_token = self.get_access_token()      
