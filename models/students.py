from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: str = None
    age: int = None
    address: dict = None

class UpdateAddress(BaseModel):
    city: str = None
    country: str = None

# class UpdateStudent(BaseModel):
#     name: str = Field(None, min_length=1, max_length=100)
#     age: int = Field(None, ge=0)
#     class UpdateAddress(BaseModel):
#         city: str = Field(None, min_length=1, max_length=100)
#         country: str = Field(None, min_length=1, max_length=100) 
# def to_dict(model_instance):
#     model_dict = model_instance.dict()
#     # Convert nested Address object to dictionary
#     model_dict['address'] = model_dict['address'].dict()
#     return model_dict