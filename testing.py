import pymongo
import certifi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_DB_URL = "mongodb+srv://abhijeetbade2000:Abhijeet2001@cluster0.vombg.mongodb.net/ABHI?retryWrites=true&w=majority&appName=Cluster0"
ca = certifi.where()

try:
    client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca, serverSelectionTimeoutMS=60000)
    # Trigger a server selection to test the connection
    client.server_info()  # Will raise an error if connection fails
    print("MongoDB connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as err:
    print("Failed to connect to MongoDB:")
    print(err)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
