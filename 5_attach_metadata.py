# Field function not only does validation but also adds metadata to the fields.
# metadata means data about data, like title, descrition, example etc.
# it describes information that gives contect to other data.
# for this we need to use Annotated from typing module
# syntax: Annotated[type, Field(...)]


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(min_length = 3, max_length = 50, title = "Patient Name", description = "Give the name of the patient in less than 50 characters", examples = ['nitish', 'amish'])]
    email: Annotated[EmailStr, Field(title = 'Email Address', description = 'Enter a valid email address')]
    linkedin_profile: AnyUrl
    age: Annotated[int, Field(ge = 20, lt = 120, title = 'Age of the patient', description = 'Age should be greater than 20 and less than 120', examples = [25,30, 45])]
    
    weight: float = Annotated[float, Field(gt = 0, lt = 500, strict = True)] # for stict type checking not pass string, tht means not to allow 'type coercion'

    married: Annotated[Optional[bool], Field(default = None , title = 'Marital Status', description = 'Is the patient married?')]
    allergies: Annotated[Optional[List[str]], Field(default = None, max_items = 5)]
    contact_details: Optional[Dict[str, str]] = Field(default = None, title = 'Contact Details', description = 'Contact details of the patient in key value pair', examples = [{'phone': '1234567890'}, {'emergency_contact': '9876543210'}])


def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('updated')
    print(patient.weight)

patient_info = {
    'name': 'rajui',
    'email': 'abc@gmail.com',
    'linkedin_profile': 'https://www.linkedin.com/in/rajui',
    'age': 30,
    'weight': '70.5'
}

patient1 = Patient(**patient_info) 

update_patient(patient1)