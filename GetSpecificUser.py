import requests
import json

def GetAllUsers(url):
    GetJson = requests.get(url).text
    data = json.loads(GetJson)
    return(data['id'])
    
def testSpecificUser():
    link = "http://jsonplaceholder.typicode.com/users/3"
    assert GetAllUsers(link) == 3 # Chech that user with ID = 3 - returned
    return