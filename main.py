#Main module that listens to API calls and
#routes them to the corresponding routes

from flask import Flask
import json
from bson import ObjectId

from routers.members_router import members
from routers.movies_router import movies
from routers.subscriptions_router import subscriptions

#Serializer class used to format data that 
#consists of data type of ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, obj) :
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self,obj)

app = Flask(__name__)


app.json_encoder = JSONEncoder

#Registering all API calls related to members who can subscribe to movies
app.register_blueprint(members, url_prefix="/members")

#Registering all API calls related to movies in the system
app.register_blueprint(movies, url_prefix="/movies")

#Registering all API calls related to subscriptions of movies by members
app.register_blueprint(subscriptions, url_prefix="/subscriptions")

app.run(port=5001)