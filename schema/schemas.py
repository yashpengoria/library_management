# from pydantic import BaseModel


# class Address(BaseModel):
#     city: str
#     country: str


# class StudentCreate(BaseModel):
#     name: str
#     age: int
#     address: Address

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "John Doe",
#                 "age": 25,
#                 "address": {
#                     "city": "New York",
#                     "country": "USA"
#                 }
#             }
#         }


# class StudentUpdate(BaseModel):
#     name: str = None
#     age: int = None
#     address: Address = None

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "Jane Smith",
#                 "age": 30
#             }
#         }


# class StudentResponse(BaseModel):
#     id: str
#     name: str
#     age: int
#     address: Address

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "id": "6117fc1317deaf103dbd0f68",
#                 "name": "John Doe",
#                 "age": 25,
#                 "address": {
#                     "city": "New York",
#                     "country": "USA"
#                 }
#             }
#         }

# def address_serial(address) ->dict:
#     return{
#         "city": address["city"],
#         "country": address["country"]
#     }

def individual_serial(student) ->dict:
    return{
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }


def list_serial(students)->dict:
    return[individual_serial(student) for student in students]