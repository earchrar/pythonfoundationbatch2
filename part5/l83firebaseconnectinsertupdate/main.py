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

    # Input document ID (string) 
    doc_id = input("Enter ID to search : ")
    new_name = input("Enter new name : ")
    new_email = input("Enter new email : ")

    # Get document reference by ID 
    doc_ref = col_ref.document(doc_id)

    # Check if document exists 
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            "username":new_name,
            "email":new_email
        })
        print("Record updated successfully.")
    else: 
        print("No record found with that ID.")

except Exception as e:
    print("Enter : ",e)