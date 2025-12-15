import pymongo # for ASCENDING and DESCENDING
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId # add this line
from dotenv import load_dotenv
from datetime import datetime,timezone
import os

load_dotenv()

try: 

    mongo_uri = os.getenv("MONGODB_URL")

    # Connect to MongoDB server 
    client = MongoClient(mongo_uri)

    # Select database and collection 
    db = client["mydatabase"]
    collection = db["employees"] 

    # Input document ID (string) 
    doc_id = input("Enter ID to search: ")

    try:
        # Convert string to ObjectID
        object_id = ObjectId(doc_id)
    except Exception as e:
        print("Invalid ID format - must be a vaild ObjectID string.")
        client.close()
        exit()

    # Get document by id 
    result = collection.find_one({"_id":object_id})

    if result:
        print(result)
    else:
        print("No record found with that ID.")

except Exception as e:
    print("Connection failed : ",e)
finally:
    client.close()

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > CRUD Operation MongoDB ( Synchronous )