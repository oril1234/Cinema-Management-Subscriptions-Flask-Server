from sqlite3 import Date
from tkinter import E
from DAL.subscriptions_db_dal import SubscriptionsDBDal
from DAL.movies_db_dal import MoviesDBDal
from DAL.members_db_dal import MembersDBDal
from bson import ObjectId

#Business logic class of the subscriptionss
# (orders of movies by members )
class SubscriptionsBL:
    def __init__(self):

        #Instance of data layer of subscriptions connected
        #to subscriptions collection
        self.__subscriptions_db_dal = SubscriptionsDBDal() 

    #Fetching all the subscription from db
    def get_all_subscriptions(self):
        subscriptions = self.__subscriptions_db_dal.get_all_subscriptions()
        return subscriptions
       
    #Get all the subscriptions of a specific member by his id
    def get_member_subscriptions(self,member_id):
       subscriptions =(
            self.__subscriptions_db_dal.get_member_subscriptions(member_id)) 
       return subscriptions

    #Add new subscription of a movie to a member
    def add_subscription(self,obj):

        #Fetching data of member's subscriptions
        member_subscriptions=self.get_member_subscriptions(
         obj["memberID"]  
        )

        #Executed if member did not subscribe to any movie
        if member_subscriptions is None:

            #Creating the first subscription by the member
            member_subscriptions={"memberID":ObjectId(obj["memberID"]),
                "subscriptions":[{"movieID":ObjectId(obj["movieID"]),
                "date":obj["date"]}],
                            }
            #Adding subscription to data base
            status = self.__subscriptions_db_dal.add_subscription(member_subscriptions)
            return status
        
        #Executed if member has already subscribed to another movies
        member_subscriptions["movies"].append(
            {"movieID":ObjectId(obj["movieID"]),
                "date":obj["date"]}
        )

        #Adding subscription to data base
        status = self.__subscriptions_db_dal.update_member_subscriptions(
            member_subscriptions["_id"], member_subscriptions)
        return status        

    #Delete all the subscription of a member by his id
    def delete_all_member_subscriptions(self,member_id):
        self.__subscriptions_db_dal.delete_member_subscriptions(member_id)

    #Delete all the subscriptions made to a specific movie using movie id
    def delete_all_movie_subscriptions(self,movie_id):
        self.__subscriptions_db_dal.delete_movie_subscriptions(movie_id)
