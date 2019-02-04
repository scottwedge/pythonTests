import requests
import pytest

### Case 1
# Select all users
print('Case 1 - Selec all users')
def GetAllUsers(url):
    return requests.get(url).status_code
    
def testGetAllUsers():
    link = "http://jsonplaceholder.typicode.com/users"
    assert GetAllUsers(link) == 200