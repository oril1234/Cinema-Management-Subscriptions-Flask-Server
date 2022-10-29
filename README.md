# Cinema Management Subscriptions Flask Server
This respository is of one of 2 cinema management system servers that provides 3 web services: 
1. Movies web service that handles all the movies shown in the cinema 
2. Members web service for people who subscribe to movies by the cinema employees 
3. Web service of Subscripttions of members to movies

The server operates against 3 data sources
1. JSON placeholder web service from which initial data of movies and members is fetched, and then stored in Mongo data base of subscriptions
2. Mongo data base that as mentioned above stores and handles data collections of movies, members, as well as the subscriptions themselves to movies by members.
Below is the architecture of the server

The server consists of 4 layers:
1.Main - The module that is the first to receive API calls
2. Routes layer - The modules the API calls are refered to from the main module
3. Business Logic Layer - The modules in which the API calls are processed, and then directed to the data layers.
4. Data layers - The modules that are called by the business logic modules in order to directly connect with Mongo Data base and JSON place holder web service.

Below is the architecture of the server as described above:
![diagram drawio (3)](https://user-images.githubusercontent.com/49225452/198851872-973235d5-9715-481a-ae9f-f7cb0c80dda9.png)


