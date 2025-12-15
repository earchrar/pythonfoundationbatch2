import pymongo
from pymongo import MongoClient
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

    # insert Data 
    datas = [
        {
            "username":"su su",
            "email":"susu@gmail.com",
            "created_At":datetime.now(timezone.utc)
        },
        {
            "username":"ni ni",
            "email":"nini@gmail.com",
            "created_At":datetime.now(timezone.utc)
        },
    ]

    # Insert a new document(auto-generated id) 
    result = collection.insert_many(datas)

    print(f"Collection {collection.name} is ready in MongoDB! Inserted ID: {result.inserted_ids} , {result.acknowledged}")
    print(f"{len(result.inserted_ids)} document inserted.")

except Exception as e:
    print("Connection failed : ",e)
finally:
    client.close()

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > CRUD Operation MongoDB ( Synchronous )