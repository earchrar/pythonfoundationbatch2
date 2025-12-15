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
    collection_name = "staffs"

    datas = [
        {
            "username":"aungaung",
            "email":"aungaung@gmail.com",
            "created_At":datetime.now()
        },
        {
            "username":"kyawkyaw",
            "email":"kyawkyaw@gmail.com",
            "created_At":firestore.SERVER_TIMESTAMP # user firebase server timestamp
        }
    ]

    batch = db.batch()

    # Create Document Method 1 
    for data in datas:
        doc_ref = db.collection(collection_name).document()
        batch.set(doc_ref,data)

    batch.commit() # commit all at once

    print(f"{len(datas)} documents inserted into Collections {collection_name} is ready in Firebase!")

except Exception as e:
    print("Enter : ",e)