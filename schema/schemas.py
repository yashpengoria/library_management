from pydantic import BaseModel, Field
from typing import Optional

class AddressUpdate(BaseModel):
    city: Optional[str]
    country: Optional[str] 

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    age: Optional[int] = Field(None, gt=0, le=150)
    address: Optional[AddressUpdate]

def individual_serial(student) ->dict:
    return{
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }


def list_serial(students)->dict:
    return[individual_serial(student) for student in students]