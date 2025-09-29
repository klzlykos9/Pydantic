# export to python dictionary or json

from pydantic import BaseModel, EmailStr
from typing import List, Dict

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address # nested model 

address_dict = {
    'city': 'delhi',
    'state': 'up',
    'pin': '3434'
}

address1 = Address(**address_dict)

patient_info = {
    'name': 'Alicia smith',
    'age': 56,
    'gender': 'Female',
    'address': address1
}

patient1 = Patient(**patient_info)   # unpacking dictionary

print(patient1)
print(patient1.address.city)  # accessing nested model field
print(patient1.address.state)
print(patient1.name)

print('*********************************************')
temp = patient1.model_dump() # conver to dictionary
print(temp)

print('*********************************************')
temp1 = patient1.model_dump_json() # convert to json
print(temp1)

print('###########################################################')
# could control fields too 

print(patient1.model_dump(include = ['name', 'gender']))   # to show only name and gender 


print(patient1.model_dump(exclude = {'age'})) # to exclude age field and show rests


print('###########################################################')
print(patient1.model_dump(exclude = {'address': ['state']}))

