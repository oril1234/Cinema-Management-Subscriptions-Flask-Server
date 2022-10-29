from DAL.movies_db_dal import MoviesDBDal
from DAL.movies_ws_dal import MoviesWSDal
from BL.subscriptions_bl import SubscriptionsBL

#Business logic class of the movies yin the system
class MoviesBL:
    def __init__(self):

        #instance of movies data layer connected to JSON placeholder
        self.__movies_ws_dal = MoviesWSDal()

        #instance of movies data layer connected to movies
        # collection in Mongo data base
        self.__movies_db_dal = MoviesDBDal()

        #instance of subscriptions data layer connected to subscriptions
        # collection in Mongo data base
        self.__subscriptions_bl=SubscriptionsBL()

        #Load data base with movies data
        self.__load_db_with_movies()
        

    #Initial load of data base with movies data fetched 
    #from JSON placeholder
    def __load_db_with_movies(self):
        movies_from_db=self.__movies_db_dal.get_all_movies()
        
        #Executed if database collection of movies is empty
        if len(movies_from_db)==0:
            movies_from_ws=self.__movies_ws_dal.get_all_movies()
            for movie in movies_from_ws:
                new_movie={"name":movie["name"],
                "genres":movie["genres"],
                "image":movie["image"]["original"],
                "premiered":movie["premiered"]}
                self.add_movie(new_movie)
        
    #Fetching all movies data from database
    def get_all_movies(self):
       movies = self.__movies_db_dal.get_all_movies()
       return movies

    #Add new movie to db
    def add_movie(self,obj):
        id = self.__movies_db_dal.add_movie(obj)
        return id

    #Update existing movie in db
    def update_movie(self,id,obj):
        obj.pop("_id",None)
        status = self.__movies_db_dal.update_movie(id,obj)
        return status

    #Delete movie by id
    def delete_movie(self,id):
        self.__subscriptions_bl.delete_all_movie_subscriptions(id)
        status = self.__movies_db_dal.delete_movie(id)
        return status