# Mimecast URL Definitions
GET_PROFILE_GROUPS_URL = "https://api.services.mimecast.com/api/directory/find-groups"
GET_GROUP_MEMBERS_URL = "https://api.services.mimecast.com/api/directory/get-group-members"

def get_profile_groups(self):
    return self.make_mimecast_request(GET_PROFILE_GROUPS_URL)

def get_group_members(self, id):
    data = [{
        "id": id
    }]
    
    return self.make_mimecast_request(GET_GROUP_MEMBERS_URL, data)
