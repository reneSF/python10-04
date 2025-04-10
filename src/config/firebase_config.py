import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Firebase Admin SDK
cred = credentials.certificate({
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n")
})

firebase_admin.initialize_app(cred)
db = firestore.client()