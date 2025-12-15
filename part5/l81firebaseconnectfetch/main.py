import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

try: 
    cred = credentials.Certificate({
        "type": os.getenv("FIREBASE_TYPE"),
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.getenv("FIREBASE_CLIENT_ID"),
        "auth_uri": os.getenv("FIREBASE_AUTH_URL"),
        "token_uri": os.getenv("FIREBASE_TOKEN_URL"),
        "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL"),
        "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
    })

    app = firebase_admin.initialize_app(cred)

    # Get firbase client 
    db = firestore.client()

    # Collection 
    collection_name = "employees"

    col_ref = db.collection(collection_name)

    # Fetch ALL 
    # docs = col_ref.order_by("created_At").stream()
    # print("\nFetch all documents\n")
    # for doc in docs:
    #     data = doc.to_dict()
    #     print(f"ID: {doc.id} , Name: {data.get('username')} , Email: {data.get('email')} , Created: {data.get('created_At')}")
    
    # Fetch SOME 
    # docs = col_ref.order_by("created_At").limit(1).stream()
    # print("\nFetch some documents\n")
    # for doc in docs:
    #     data = doc.to_dict()
    #     print(f"ID: {doc.id} , Name: {data.get('username')} , Email: {data.get('email')} , Created: {data.get('created_At')}")

    # Fetch ONE 
    doc = col_ref.order_by("created_At").limit(1).get()
    # print(docs)
    print("\nFetch one documents\n")

    if doc: 
        data = doc[0].to_dict()
        print(f"ID: {doc[0].id} , Name: {data.get('username')} , Email: {data.get('email')} , Created: {data.get('created_At')}")

except Exception as e:
    print("Enter : ",e)