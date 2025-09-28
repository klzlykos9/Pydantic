from pydantic import BaseModel

# type validation using pydantic

# 1st step
class Patient(BaseModel):
    name: str
    age: int

# 2nd step
patient_info = {'name': 'nitish', 'age': 28}

patient1 = Patient(**patient_info)

# 3rd Step
def insert_patient_data2(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

# now check it 
insert_patient_data2(patient1)