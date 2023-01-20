# creating connection to mongodb database

def connect_to_database():
    import os
    from pymongo import MongoClient

    password = os.environ.get("MONGODB_PWD")
    connection_string = f"mongodb://localhost:27017"
    client = MongoClient(connection_string)
    print("Successfully connected to database!")
    return client
