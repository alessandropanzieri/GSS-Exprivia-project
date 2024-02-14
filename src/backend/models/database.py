from pymongo.mongo_client import MongoClient

def get_database():
    cluster = MongoClient("mongodb+srv://username:dalEpB6lf0fPCucs@cluster.f653jhv.mongodb.net/?retryWrites=true&w=majority")
    return cluster.gss_db