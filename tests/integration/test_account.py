# Standard Python modules
from dotenv import load_dotenv
import os
import pytest

# Local Python modules
from pymime import PyMime

# Load environment variables for testing
load_dotenv()

@pytest.fixture
def mimecast():
    return PyMime(client_id=os.environ["MIMECAST_CLIENT_ID"], client_secret=os.environ["MIMECAST_CLIENT_SECRET"])

def test_get_account(mimecast):
    # Call the method
    account_info = mimecast.get_account()

    # Assertions
    assert len(account_info["data"]) > 0
    
def test_get_dashboard_notifications(mimecast):
    # Call the method
    notifications = mimecast.get_dashboard_notifications()

    # Assertions
    assert "data" in notifications
    assert notifications["meta"]["status"] == 200
    
def test_get_support_info(mimecast):
    # Call the method
    support_info = mimecast.get_support_info()
    print(support_info)

    # Assertions
    assert len(support_info["data"]) > 0
    assert support_info["meta"]["status"] == 200
