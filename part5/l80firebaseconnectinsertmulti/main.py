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
        ("maungmaung","maungmaung@gmail.com"),
        ("mama","mama@gmail.com")
    ]

    batch = db.batch()

    # Create Document Method 1 (i)
    for x in range(len(datas)):
        username = datas[x][0]
        email = datas[x][1]
        doc_ref = db.collection(collection_name).document()
        batch.set(doc_ref,{
            "username":username,
            "email":email,
            "created_At":firestore.SERVER_TIMESTAMP
        })

    # Create Document Method 1 (ii)
    # for username,email in datas:
    #     doc_ref = db.collection(collection_name).document()
    #     batch.set(doc_ref,{
    #         "username":username,
    #         "email":email,
    #         "created_at":datetime.now()
    #     })

    batch.commit() # commit all at once

    print(f"{len(datas)} documents inserted into Collections {collection_name} is ready in Firebase!")

except Exception as e:
    print("Enter : ",e)