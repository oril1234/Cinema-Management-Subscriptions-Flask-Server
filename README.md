# Cinema Management Subscriptions Flask Server
This respository is of one of 2 cinema management system servers that provides 3 web services: 
1. Movies web service that handles all the movies shown in the cinema 
2. Members web service for people who subscribe to movies by the cinema employees 
3. Web service of Subscripttions of members to movies

The server operates against 3 data sources
1. JSON placeholder web service from which initial data of movies and members is fetched, and then stored in Mongo data base of subscriptions
2. Mongo data base that as mentioned above stores and handles data collections of movies, members, as well as the subscriptions themselves to movies by members.

The server consists of 4 layers:
1. Main - The module that is the first to receive API calls
2. Routes layer - The modules the API calls are refered to from the main module
3. Business Logic Layer - The modules in which the API calls are processed, and then directed to the data layers.
4. Data layers - The modules that are called by the business logic modules in order to directly connect with Mongo Data base and JSON place holder web service


Below is the architecture of the server as described above:
![diagram drawio (5)](https://user-images.githubusercontent.com/49225452/198852210-f3dfe77c-855e-4903-8944-08e1f64d9bf6.png)

### Requirements
Python 3.8.+

### Install Requirements
- pip install requests
- pip install pymongo

[https://twitter.com/home?lang=eng](Press Here)
