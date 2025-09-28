from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name', mode = 'before')
    @classmethod
    def name_uppercase(cls, value):
        return value.upper()
    
    @field_validator('age', mode = 'before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else :
            raise ValueError('Age should be between 0 and 100')
   

def update_patient(patient: Patient):
    print(f'Name: {patient.name}')
    print(f'Age: {patient.age}')
    print(f'Email: {patient.email}')
    print('updated ✅ ')

patient_info = {
    'name' : 'john doe',
    'email': 'abc@icici.com',
    'age': '30',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '235434343'}
}

pateint1 = Patient(**patient_info)

update_patient(pateint1)