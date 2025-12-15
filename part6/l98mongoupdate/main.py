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
    doc_id = input("Enter document ID to update : ").strip() 
    new_name = input("Enter new name : ").strip()
    new_email = input("Enter new email : ").strip()

    try:
        # Convert string to ObjectID
        object_id = ObjectId(doc_id)
    except Exception as e:
        print("Invalid ID format - must be a vaild ObjectID string.")
        client.close()
        exit()

    query_filter = {"_id":object_id}

    update_operation = {
        "$set":{
            "username":new_name,
            "email":new_email
        }
    }

    # Get document by id 
    result = collection.update_one(query_filter,update_operation)

    if result.matched_count > 0:
        print(f"Update successfully. Modified count : {result.modified_count}")
    else:
        print("No record found with that ID.")

except Exception as e:
    print("Connection failed : ",e)
finally:
    client.close()

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > CRUD Operation MongoDB ( Synchronous )