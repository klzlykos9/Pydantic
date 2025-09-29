"""
if patient age is greater than 60 then add a emergency phone number in thier contact details .
otherwise not to admit tht patient . 
here we hv to check 2 field for validating , so here we ll use model validator .

"""
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    
def update_patient_data(patient: Patient):
    print(f'Patient Name: {patient.name}')
    print(f'Patient Age: {patient.age}')
    print(f'Patient Email: {patient.email}')
    print(f'Patient Contact Details: {patient.contact_details}')
    print(f'Patient Allergies: {patient.allergies}')
    print('Patient data updated sucessfully')


patient_info = {
    'name': 'Alicia Smith',
    'email': 'alicia_smith@gmail.com',
    'age': 65,
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '343542343', 'emergency': '35435345435'}
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

