
from faker import Faker
import random


from dataclasses import dataclass


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()

@dataclass
class Color:
    color_name: list = None



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


@dataclass
class Date:
    day: int = None
    month: int = None
    year: int = None
    time: int = None


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


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow","Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]


    )

def generated_date():
    yield Date (
        year = faker_en.year(),
        month = faker_en.month_name(),
        day = faker_en.day_of_month(),
        time = '12:15'
    )


