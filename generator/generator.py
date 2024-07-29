
from faker import Faker
import random


from dataclasses import dataclass



faker_ru = Faker('ru_RU')
Faker.seed()




@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None






def generated_person():

    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname= faker_ru.first_name(),
        lastname = faker_ru.last_name(),
        age =random.randint(10,80),
        salary= random.randint(10,1000),
        department = faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile= faker_ru.msisdn(),
    )

def generate_file():
        path = rf'C:\INSTALL\filename{random.randint(0,99)}.txt'
        file = open(path, 'w+')
        file.write(f'WW3 is now{random.randint(0,99)} ')
        file.close()
        return file.name, path


