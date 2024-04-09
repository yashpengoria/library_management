from fastapi import APIRouter, HTTPException
from models.students import Student
from config.database import collection_name
from schema.schemas import list_serial, StudentUpdate
from bson import ObjectId

router= APIRouter()

@router.get("/", include_in_schema=False)
async def read_root():
    return {"message": "Go to https://library-management-gj13.onrender.com/docs to check out APIs"}


#GET Request Method
@router.get("/students")
async def get_students(country: str = None, age: int =None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = list_serial(collection_name.find(query))
    return {"data": students}


#POST Request method
@router.post("/students")
async def post_students(student: Student):
    student_dict=student.dict()
    student_dict['address']=student.address.dict()
    collection_name.insert_one(student.dict())
    return {"message": "Student added successfully"}


#GET BY ID Request method
@router.get("/students/{id}")
async def get_student_by_id(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")

        student_data = collection_name.find_one({"_id": ObjectId(id)})

        if student_data is None:
            raise HTTPException(status_code=404, detail="Student not found")

        student_data['_id'] = str(student_data['_id'])

        return student_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

 
# PATCH Request Method
@router.patch("/students/{id}")
async def update_student_by_id(id: str, student: StudentUpdate):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")
        
        update_dict = student.dict(exclude_unset=True)
        
        result = collection_name.update_one({"_id": ObjectId(id)}, {"$set": update_dict})
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")



    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")

        update_dict = {}
        
        # Update name if provided
        if student.name is not None:
            update_dict["name"] = student.name
        
        # Update age if provided
        if student.age is not None:
            update_dict["age"] = student.age

        # Update address if provided
        if student.address is not None:
            update_dict["address"] = student.address.dict()

        if not update_dict:
            raise HTTPException(status_code=400, detail="No fields provided for update")

        # Update the student in the MongoDB collection
        result = collection_name.update_one({"_id": ObjectId(id)}, {"$set": update_dict})
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student updated successfully"}

    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")



# DELETE Request method to delete a student by ID
@router.delete("/students/{id}")
async def delete_student_by_id(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid student ID")

        result = collection_name.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
