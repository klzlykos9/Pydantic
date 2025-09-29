
"""
computed fields e.g. calculate bmi = hieght/weight
which is computed from other fields.

"""


from pydantic import BaseModel, Field, EmailStr, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field     # called as decorator
    @property
    def calculated_bmi(self) ->  float:
        bmi = round((self.weight)/ (self.height**2), 2)
        return bmi
    

def update_patient_data(patient: Patient):
    print(f'Patient Name: {patient.name}')
    print(f'Patient Age: {patient.age}')
    print(f'Patient Email: {patient.email}')
    print(f'Patient Contact Details: {patient.contact_details}')
    print(f'Patient Allergies: {patient.allergies}')
    print(f'Patient BMI: {patient.calculated_bmi}')
    print('Patient data updated sucessfully')


patient_info = {
    'name': 'Alicia Smith',
    'email': 'alicia_smith@gmail.com',
    'age': 65,
    'weight': 70.5,
    'height': 1.75,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '343542343', 'emergency': '35435345435'}

}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
