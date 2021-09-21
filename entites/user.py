from faker import Faker
from .base_entity import BaseEntity, BaseGenerateRandom


class User(BaseEntity):

    def __init__(self, email, first_name, last_name, age, address, gender, job, has_children_under_sixteen):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender
        self.job = job
        self.has_children_under_sixteen = has_children_under_sixteen


class GenerateRandomUser(BaseGenerateRandom):
    @staticmethod
    def generate_random():
        fake = Faker()
        fake_gender = fake.random_element(elements=('F', 'M'))
        fake_age = fake.pyint(min_value=12, max_value=85, step=1)
        fake_first_name = fake.first_name_female() if fake_gender == 'F' else fake.first_name_male()
        fake_last_name = fake.last_name_female() if fake_gender == 'F' else fake.last_name_male()

        return User(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake.email(),
            address=fake.address(),
            age=fake_age,
            job=fake.job(),
            gender=fake_gender,
            has_children_under_sixteen=fake.pybool() if 18 <= fake_age < 60 else False
        )


# Test user generate
if __name__ == '__main__':
    print(GenerateRandomUser().generate_random().to_json())
