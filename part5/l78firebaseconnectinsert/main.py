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

    data = {
        "username":"aungaung",
        "email":"aungaung@gmail.com",
        # "created_At":datetime.now()
        "created_At":firestore.SERVER_TIMESTAMP # user firebase server timestamp
    }

    # # Create Document Method 1 
    # doc_ref = db.collection(collection_name).document("test_dockey")
    # doc_ref.set(data)

    # Create Document Method 2 , Push a new document with auto-generated ID 
    doc_ref = db.collection(collection_name).add(data)

    print(f"Collection {collection_name} is ready in Firebase!")

except Exception as e:
    print("Enter : ",e)