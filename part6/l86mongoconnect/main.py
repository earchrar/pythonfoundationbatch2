from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try: 

    mongo_uri = os.getenv("MONGODB_URL")

    # Connect to MongoDB server 
    client = MongoClient(mongo_uri)

    client.admin.command({'ping': 1})
    print("Connected Successfully")

except Exception as e:
    print("Connection failed : ",e)
finally:
    client.close()

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > Connect ( Synchronous )