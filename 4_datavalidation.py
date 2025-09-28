from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional

# for custom data validation hv to use Field

class Patient(BaseModel):
    name: str = Field(min_length = 3, max_length = 50)
    age: int = Field(ge = 20, lt = 120) # age should be greater than 20 and less than 120
    linkedin_profile: AnyUrl
    weight: float = Field(gt = 0, lt = 500) # weight should be greater than 0 and less than 500
    email: EmailStr
    married: bool
    allergies: Optional[List[str]] = Field(default = None, max_items = 5) # max 5 allergies

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated')


patient_info = {
    'name': 'john doe',
    'age': 30,
    'weight': 70.5,
    'email': 'abcfieji@gmail.com',
    'married': False,
    'linkedin_profile': 'https://www.linkedin.com/in/johndoe',

}

patient = Patient(**patient_info)
update_patient(patient)