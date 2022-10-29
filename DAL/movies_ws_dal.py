import requests

#Movies data layer class connected to JSON placeholder 
class MoviesWSDal:
    def __init__(self):

        #URL og JSON placeholder
        self.__url = "https://jsonplaceholder.typicode.com/users"

    #Fetching all movies from JSON placeholder
    def get_all_movies(self):
        resp = requests.get(self.__url)
        return resp.json()