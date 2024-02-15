from pymongo.mongo_client import MongoClient

def get_database():
    cluster = MongoClient("mongodb://mongodb:27017")
    return cluster.gss_db