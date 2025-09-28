from pydantic import BaseModel
from typing import List, Dict

# 1st  step (type validation using pydantic)

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]   # list of strings
    contact_details: Dict[str, str]  # dictionary with string keys and string values

# 2nd step

def inserted_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted into database sucessfully.')

# 3rd step
patient_info = {
    'name': 'nitish',
    'age': 28,
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'nuts', 'dust'],
    'contact_details': {'email': 'nitish@gmail.com', 'phone': '3434234234'}
}

patint1 = Patient(**patient_info)

inserted_patient_data(patint1)