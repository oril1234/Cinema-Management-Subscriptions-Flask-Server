from pymongo import MongoClient
from bson import ObjectId

#Movies data layer class connected to Mongo data base
#collection of movies
class MoviesDBDal:
    def __init__(self):

        #Connection of Mongo DB
        self.__client = MongoClient(port=27017)

        #Data base of subscriptions in which the collection
        #of movies is located
        self.__db = self.__client["subscriptionsDB"]

        #Collection of movies
        self.__collection=self.__db["movies"]

    #fetching all the movies from data base
    def get_all_movies(self):
        arr = []
        arr = list(self.__collection.find({}))
        return arr

    #Add new movie to data base
    def add_movie(self,obj):
        self.__collection.insert_one(obj)
        return str(obj["_id"])

    #Update existing movie in data base
    def update_movie(self,id,obj):
        self.__collection.update_one({"_id" : ObjectId(id)}, {"$set" : obj})
        return 'Updated!' 

    #Delete movie from data base by the movie id
    def delete_movie(self,id):
        self.__collection.delete_one({"_id" : ObjectId(id)})
        return 'Deleted!'  
