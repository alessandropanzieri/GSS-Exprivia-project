# database.py
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection
try:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["cluster.gss_db"]
    employees_collection = db["employees"]
    administrative_collection = db["administrative_collection"]
    event_collection = db["event_collection"]
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")
