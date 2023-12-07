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

def test_get_profile_groups(mimecast):
    # Get all the profile groups
    profile_groups = mimecast.get_profile_groups()

    # Assertions
    assert profile_groups is not None
    assert len(profile_groups["data"]) > 0

def test_get_group_members(mimecast):
    # Get the profile groups and select the first one
    profile_groups = mimecast.get_profile_groups()
    test_group_id = profile_groups["data"][0]["folders"][0]["id"]
    
    group_members = mimecast.get_group_members(test_group_id)

    # Assertions
    assert group_members is not None
    assert len(group_members["data"]) > 0
