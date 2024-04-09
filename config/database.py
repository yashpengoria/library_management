from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODBURL=os.getenv("MONGODBURL")

client=MongoClient(MONGODBURL)

db=client.student_db
collection_name= db["students"]