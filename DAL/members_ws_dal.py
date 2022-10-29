import requests

#Members data layer class connected to JSON placeholder 
class MembersWSDal:
    def __init__(self):

        #URL og JSON placeholder
        self.__url = "https://jsonplaceholder.typicode.com/users"

    #Fetching all members from JSON placeholder
    def get_all_members(self):
        resp = requests.get(self.__url)
        return resp.json()