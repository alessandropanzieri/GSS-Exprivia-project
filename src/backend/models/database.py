from os import getenv
from pymongo.mongo_client import MongoClient

def get_database():
    cluster = MongoClient(getenv("MONGODB_SERVER_URL"))
    return cluster.gss_db