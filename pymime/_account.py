# Mimecast API URLS
GET_ACCOUNT_URL = "https://api.services.mimecast.com/api/account/get-account"
GET_DASHBOARD_NOTIFICATIONS_URL = "https://api.services.mimecast.com/api/account/get-dashboard-notifications"
GET_SUPPORT_INFO_URL = "https://api.services.mimecast.com/api/account/get-support-info"

def get_account(self):
    account_info = self.make_mimecast_request(GET_ACCOUNT_URL)
    self.account_code = account_info["data"][0]["accountCode"]
    
    return account_info

def get_dashboard_notifications(self):
    if not hasattr(self, "account_code") or self.account_code is None:
        self.get_account()
    
    data = [{
        "accountCode": self.account_code,
    }]
    notifications = self.make_mimecast_request(GET_DASHBOARD_NOTIFICATIONS_URL, data=data)
    
    return notifications

def get_support_info(self):
    support_info = self.make_mimecast_request(GET_SUPPORT_INFO_URL)

    return support_info
