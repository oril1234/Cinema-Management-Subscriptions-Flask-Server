from pymongo import MongoClient
from bson import ObjectId

#Subscriptions data layer class connected to Mongo data base
class SubscriptionsDBDal:
    def __init__(self):

        #Connection of Mongo DB
        self.__client = MongoClient(port=27017)

        #Data base of subscriptions in which the collection
        #of members subscriptions is located
        self.__db = self.__client["subscriptionsDB"]

        #Collection of members subscriptions
        self.__collection=self.__db["membersSubscriptions"]

    #Fetching all the members in the system
    def get_all_subscriptions(self):
        arr = []
        arr = list(self.__collection.find({}))
        return arr

    #Get all the subscriptions of a specific member by his id
    def get_member_subscriptions(self,member_id):
        subscription = self.__collection.find_one({ "memberID" :ObjectId(member_id) })
        return subscription

    #Adding new subscription of member to data base
    def add_subscription(self,obj):
        self.__collection.insert_one(obj)
        return 'Created with ID ' + str(obj["_id"])    


    #Delete all the subscriptions of a member by his id
    def delete_member_subscriptions(self,member_id):
        self.__collection.delete_one({"memberID" : ObjectId(member_id)})
        return 'Deleted!'  

    #Delete all the subscriptions to a movie by its id
    def delete_movie_subscriptions(self,movie_id):
        self.__collection.update_many(
            { },
            {
                "$pull": { "movies": { "movieID" : ObjectId(movie_id)} }
            }
        )
        return 'Deleted!'  