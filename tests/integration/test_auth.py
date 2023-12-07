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

def test_get_access_token(mimecast):
    # Call the method
    mimecast.access_token = mimecast.get_access_token()

    # Assertions
    assert mimecast.access_token is not None

