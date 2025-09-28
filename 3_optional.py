# Optional Pydantic integration

from typing import List, Dict, Optional
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies if patient.allergies else "No allergies provided")


patient_info = {
    'name': 'nitish',
    'age': 28,
    'weight': 70.5,
    'married': True,
    'contact_details': {'email': 'abc@gmail.com', 'phone': '3434234234'}
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)