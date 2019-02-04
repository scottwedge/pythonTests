import requests
import pytest

### Case 3
# Create user 

def GetAllUsers(url):
    return requests.post(url).status_code
    
def testGetAllUsers():
    link = "http://jsonplaceholder.typicode.com/users"
    assert GetAllUsers(link) == 201

