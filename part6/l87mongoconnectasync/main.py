import asyncio
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    try: 

        mongo_uri = os.getenv("MONGODB_URL")

        # Connect to MongoDB server 
        client = AsyncMongoClient(mongo_uri)

        await client.admin.command({'ping': 1})
        print("Connected Successfully")

    except Exception as e:
        print("Connection failed : ",e)
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())

# Documents > Client Library > Python > Pymongo or "Get started with MongoDB Python" > Get Started > Connect ( Asynchronous )