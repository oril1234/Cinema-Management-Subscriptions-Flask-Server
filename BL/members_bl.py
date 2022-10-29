from DAL.members_db_dal import MembersDBDal
from DAL.members_ws_dal import MembersWSDal
from BL.subscriptions_bl import SubscriptionsBL

#Business logic class of the members 
# (people who subscribe to mmovies) in the system
class MembersBL:
    def __init__(self):

        #instance of members data layer connected to JSON placeholder
        self.__members_ws_dal = MembersWSDal()

        #instance of members data layer connected to members
        # collection in Mongo data base
        self.__members_db_dal = MembersDBDal()

        #instance of subscriptions data layer connected to subscriptions
        # collection in Mongo data base
        self.__subscriptions_bl=SubscriptionsBL()

        #Load data base with members data
        self.__load_db_with_members()
        

    #Initial load of data base with members data fetched 
    #from JSON placeholder
    def __load_db_with_members(self):
        members_from_db=self.__members_db_dal.get_all_members()
        
        #Executed if database collection of members is empty
        if len(members_from_db)==0:
            members_from_ws=self.__members_ws_dal.get_all_members()
            for member in members_from_ws:
                new_member={"name":member["name"],"email":member["email"],
                "city":member["address"]["city"]}
                self.add_member(new_member)
        
    #Fetching all members data from database
    def get_all_members(self):
       members = self.__members_db_dal.get_all_members()
       return members

    #Add new member to db
    def add_member(self,obj):
        id = self.__members_db_dal.add_member(obj)
        return id

    #Update existing member in db
    def update_member(self,id,obj):
        obj.pop("_id",None)
        status = self.__members_db_dal.update_member(id,obj)
        return status

    #Delete member by id
    def delete_member(self,id):
        self.__subscriptions_bl.delete_all_member_subscriptions(id)
        status = self.__members_db_dal.delete_member(id)
        return status