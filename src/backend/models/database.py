from os import getenv
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

def get_database():
    cluster = MongoClient(getenv("MONGODB_SERVER_URL"))
    return cluster.gss_db