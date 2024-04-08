from fastapi import APIRouter, HTTPException
from models.students import Student, UpdateStudent
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router= APIRouter()


#GET Request Method
@router.get("/students")
async def get_students():
    students=list_serial(collection_name.find())
    return students


#POST Request method
@router.post("/students")
async def post_students(student: Student):
    student_dict=student.dict()
    student_dict['address']=student.address.dict()
    collection_name.insert_one(student.dict())


#GET BY ID Request method
@router.get("/students/{id}")
async def get_student_by_id(id: str):
    try:
        # Check if the provided student_id is a valid ObjectId
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")

        # Query the MongoDB collection to find the student by ID
        student_data = collection_name.find_one({"_id": ObjectId(id)})

        # If student with provided ID doesn't exist, return 404 Not Found
        if student_data is None:
            raise HTTPException(status_code=404, detail="Student not found")

        # Convert ObjectId to string
        student_data['_id'] = str(student_data['_id'])

        # Return the student data
        return student_data
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")
    
#PATCH Request Method
# @router.patch("/students/{id}")
# async def update_student_by_id(id: str, student: Student):
#     try:
#         if not ObjectId.is_valid(id):
#             raise HTTPException(status_code=400, detail="Invalid student ID")
        
#         # Update the student in the MongoDB collection
#         result = collection_name.update_one({"_id": ObjectId(id)}, {"$set": student.dict()})


#     except Exception as e:
#         # Handle any other unexpected errors
#         raise HTTPException(status_code=500, detail="Internal server error")
@router.patch("/students/{id}")
async def update_student_by_id(id: str, student_data: UpdateStudent):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")
        
        student=collection_name.find_one({"_id": ObjectId(id)})

        if student_data.name:
            student.name = student_data.name
        if student_data.age:
            student.age = student_data.age
        if student_data.address:
            if student_data.address.city:
                student.address.city = student_data.address.city
            if student_data.address.country:
                student.address.country = student_data.address.country

        # Save the updated student object back to the database
        student.save()

        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# DELETE Request method to delete a student by ID
@router.delete("/students/{id}")
async def delete_student_by_id(id: str):
    try:
        # Check if the provided student_id is a valid ObjectId
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")

        # Delete the student from the MongoDB collection
        result = collection_name.delete_one({"_id": ObjectId(id)})

        # If no matching student was found, return 404 Not Found
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        # Return a success message
        return {"message": "Student deleted successfully"}
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")
