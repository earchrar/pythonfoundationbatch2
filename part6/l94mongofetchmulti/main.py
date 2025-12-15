import pymongo # for ASCENDING and DESCENDING
from pymongo import MongoClient
from pprint import pprint
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

    count = collection.count_documents({})
    print(f"Total documents count : {count}")
    
    # FETCH ALL 
    # print("\n Fetch Fetch all documents \n")
    # results = collection.find().sort("created_At",pymongo.ASCENDING) # ASCENDING
    # results = collection.find().sort("created_At",pymongo.DESCENDING) # DESCENDING
    # results = collection.find({}).sort("created_At",pymongo.DESCENDING) # DESCENDING

    # for result in results:
    #     # print({
    #     #     "ID":str(result.get("_id")),
    #     #     "Name":result.get("username"),
    #     #     "Email":result.get("email"),
    #     #     "Created_At":result.get("created_At"),
    #     # })

    #     pprint({
    #         "ID":str(result.get("_id")),
    #         "Name":result.get("username"),
    #         "Email":result.get("email"),
    #         "Created_At":result.get("created_At"),
    #     })

    # FETCH SOME 
    # print("\n Fetch Fetch some documents \n")
    # results = collection.find({}).sort("created_At",pymongo.DESCENDING).limit(2) # DESCENDING

    # for result in results:
    #     # print({
    #     #     "ID":str(result.get("_id")),
    #     #     "Name":result.get("username"),
    #     #     "Email":result.get("email"),
    #     #     "Created_At":result.get("created_At"),
    #     # })

    #     pprint({
    #         "ID":str(result.get("_id")),
    #         "Name":result.get("username"),
    #         "Email":result.get("email"),
    #         "Created_At":result.get("created_At"),
    #     })

    # FETCH ONE 
    print("\n Fetch Fetch first documents \n")
    results = collection.find({}).sort("created_At",pymongo.DESCENDING).limit(1) # DESCENDING

    # first_doc = results.to_list() 
    first_doc = results.to_list(length=1)

    if first_doc:
        print({
            "ID":str(first_doc[0].get("_id")),
            "Name":first_doc[0].get("username"),
            "Email":first_doc[0].get("email"),
            "Created_At":first_doc[0].get("created_At")
        })
    else:
        print("No documents found!")

except Exception as e:
    print("Connection failed : ",e)
finally:
    client.close()

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > CRUD Operation MongoDB ( Synchronous )