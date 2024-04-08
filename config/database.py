from pymongo import MongoClient

client=MongoClient("mongodb+srv://yashpengoria0505:BYNpp0360G@cluster0.ugca3bc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.student_db
collection_name= db["students"]