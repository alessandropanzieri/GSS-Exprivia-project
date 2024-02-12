from os import environ
from pymongo.mongo_client import MongoClient

def get_database():
    cluster = MongoClient(environ.get("DATABASE_URL"))
    return cluster.gss_db