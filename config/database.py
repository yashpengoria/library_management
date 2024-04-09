from pymongo import MongoClient
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

encoded_username = urllib.parse.quote_plus(os.getenv("username"))
encoded_password = urllib.parse.quote_plus(os.getenv("password"))

# Construct the MongoDB URI with the encoded username and password


MONGODBURL = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.skqct13.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MONGODBURL=os.getenv("MONGODBURL")

client=MongoClient(MONGODBURL)

db=client.student_db
collection_name= db["students"]