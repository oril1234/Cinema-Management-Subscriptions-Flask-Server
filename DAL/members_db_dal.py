from pymongo import MongoClient
from bson import ObjectId

#Members data layer class connected to Mongo
#data base collection of members
class MembersDBDal:
    def __init__(self):

        #Connection of Mongo DB
        self.__client = MongoClient(port=27017)

        #Data base of subscriptions in which the collection
        #of members is located
        self.__db = self.__client["subscriptionsDB"]

        #Collection of members
        self.__collection=self.__db["members"]

    #fetching all the members from data base
    def get_all_members(self):
        arr = []
        arr = list(self.__collection.find({}))
        return arr

    #Add new member to data base
    def add_member(self,obj):
        self.__collection.insert_one(obj)
        return str(obj["_id"])

    #Update existing member in data base
    def update_member(self,id,obj):
        self.__collection.update_one({"_id" : ObjectId(id)}, {"$set" : obj})
        return 'Updated!' 

    #Delete member from data base by the member id
    def delete_member(self,id):
        self.__collection.delete_one({"_id" : ObjectId(id)})
        return 'Deleted!'  
