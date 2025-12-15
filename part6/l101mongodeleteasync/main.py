import asyncio
import pymongo
from pymongo import AsyncMongoClient
from bson import ObjectId # add this line
from dotenv import load_dotenv
from datetime import datetime,timezone
import os

load_dotenv()

async def main():
    try: 

        mongo_uri = os.getenv("MONGODB_URL")

        # Connect to MongoDB server 
        client = AsyncMongoClient(mongo_uri)

        # Select database and collection 
        db = client["mydatabase"]
        collection = db["employees"] 

        # Input document ID (string) 
        doc_id = input("Enter document ID to delete : ").strip() 

        try:
            # Convert string to ObjectID
            object_id = ObjectId(doc_id)
        except Exception as e:
            print("Invalid ID format - must be a vaild ObjectID string.")
            client.close()
            exit()

        query_filter = {"_id":object_id}

        # Get document by id 
        result = await collection.delete_one(query_filter)

        if result.deleted_count > 0:
            print(f"Delete successfully. Delete count {result.deleted_count}")
        else:
            print("No record found with that ID.")

    except Exception as e:
        print("Connection failed : ",e)
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > CRUD Operation MongoDB ( Synchronous )