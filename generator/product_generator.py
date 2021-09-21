from random import Random
from time import sleep

from entites.product import GenerateRandomProduct


class ProductGenerator:

    @staticmethod
    def generate(amount_of_batches=10, batch_size_from=50, batch_size_to=100):
        for i in range(0, amount_of_batches):
            products = list()
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f"Batch # {i} size {batch_size}")
            for _ in range(0, batch_size):
                products.append(GenerateRandomProduct.generate_random())
            yield products
        sleep(5)
