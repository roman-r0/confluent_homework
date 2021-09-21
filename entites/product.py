from faker import Faker
from .base_entity import BaseEntity, BaseGenerateRandom

CATEGORIES = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

PRODUCTS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]


class Product(BaseEntity):

    def __init__(self, name, category, price, barcode, description):
        self.name = name
        self.category = category
        self.price = price
        self.barcode = barcode
        self.description = description


class GenerateRandomProduct(BaseGenerateRandom):
    @staticmethod
    def generate_random():
        fake = Faker()

        return Product(
            name=fake.random_element(PRODUCTS),
            category=fake.random_element(CATEGORIES),
            price=fake.pyfloat(positive=True, max_value=100000),
            barcode=int(fake.ean(length=8)),
            description=fake.sentence(nb_words=10)
        )


# Test user generate
if __name__ == '__main__':
    print(GenerateRandomProduct().generate_random().to_json())
