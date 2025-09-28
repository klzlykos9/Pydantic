from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Optional, Dict, Annotated


"""
There is a situation hwre this hopital hving banks as their client.
so some bank have the polity that they could get a discount price.
so here we hv to validate the field based on some condition. and varify tht the customer is a bank employee or not .
for this we hv to use custom validator to check whether the customer is hiving bank mail id or not e.g. @hdfc or @icici etc.
also we could do some transformation on the field too e.g. we want name in uppercase or lowercase.
"""

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]



    # validate email and check if bank employee or not
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name') # by default it is post validation, mode = 'after, that means i am getting data after all validation and parsing is done.(e.g. type coercion is done.) if mode = 'before' then it will get data before any validation or parsing is done.
    @classmethod
    def name_uppercase(cls, value):
        return value.upper()

def update_patient(patient: Patient):
    print("Name: ",patient.name)
    print('Age: ',patient.age)
    print('Email: ', patient.email)
    print('updated ✅')

patient_info = {
    'name': 'john doe',
    'email': 'abc@hdfc.com',
    'age': 30,
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '23435343433'}
                }   

patient1 = Patient(**patient_info) # validation -> type certion -> custom validation -> object creation (performs here)

update_patient(patient1)


"""
field validator operates in two mode: (before and after)
1. pre: it validates the data before any other validation or parsing is done.
2. post: it validates the data after all other validation and parsing is done.

"""