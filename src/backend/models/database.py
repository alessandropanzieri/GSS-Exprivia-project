from os import environ
from pymongo.mongo_client import MongoClient

def get_database():
    cluster = MongoClient("mongodb://localhost:27017")
    return cluster.gss_db