from pydantic import BaseModel

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
    'pin': '34343'
}

address1 = Address(**address_dict)

patient_info = {
    'name': 'Alicia Smith',
    'age': 65,
    'gender': 'Female',
    'address': address1
}

patient1 = Patient(**patient_info)    # unpacking dictionary

print(patient1)
print(patient1.address.city)  # accessing nested model field
print(patient1.address.state)
print(patient1.name)


# Better organization of related data (e.g. vitals, adres, insurance)

# Reusability: Use vitals in multiple models (e.g. Patient, MedicalRecord)
# Readablility: Easier for developers and API consumers to understand structure
# Validation: Nested models are validated automatically-no extra work needed