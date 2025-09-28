"""
creating a function where we recieve patients data and inserting in database 
2. i could use type hinting to hint bout data types.

"""
def insert_patent_data(name: str, age: int):
    print(name)
    print(age)
    print('inserted into database.')




"""
to strictly inforce data type.


"""

def insert_patient_data1(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('inserted into database sucessfully.')
    else:
        raise TypeError('Incorrect data type')
    
insert_patient_data1('john', '28')