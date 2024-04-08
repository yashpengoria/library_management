from fastapi import FastAPI
from routes.route import router

app=FastAPI()

app.include_router(router)
# from fastapi import FastAPI, Query, Path, HTTPException
# from pymongo import MongoClient
# from bson import ObjectId
# from schema.schemas import StudentCreate, StudentUpdate, StudentResponse

# app = FastAPI()
# client = MongoClient("mongodb+srv://yashpengoria0505:BYNpp0360G@cluster0.ugca3bc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db = client["library"]
# collection = db["students"]


# @app.post("/students", response_model=StudentResponse)
# def create_student(student: StudentCreate):
#     inserted_student = collection.insert_one(student.dict())
#     return {"id": str(inserted_student.inserted_id), **student.dict()}


# @app.get("/students", response_model=dict)
# def list_students(country: str = None, age: int = None):
#     query = {}
#     if country:
#         query["address.country"] = country
#     if age:
#         query["age"] = {"$gte": age}
#     students = list(collection.find(query))
#     return {"data": students}


# @app.get("/students/{id}", response_model=StudentResponse)
# def get_student(id: str):
#     student = collection.find_one({"_id": ObjectId(id)})
#     if student:
#         return student
#     else:
#         raise HTTPException(status_code=404, detail="Student not found")


# @app.patch("/students/{id}", response_model=dict)
# def update_student(id: str, student: StudentUpdate):
#     updated_student = collection.update_one(
#         {"_id": ObjectId(id)},
#         {"$set": student.dict(exclude_unset=True)}
#     )
#     if updated_student.modified_count == 0:
#         raise HTTPException(status_code=404, detail="Student not found")
#     else:
#         return {}


# @app.delete("/students/{id}", response_model=dict)
# def delete_student(id: str):
#     deleted_student = collection.delete_one({"_id": ObjectId(id)})
#     if deleted_student.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Student not found")
#     else:
#         return {}


