from random import Random
from time import sleep

from entites.user import GenerateRandomUser


class UserGenerator:

    @staticmethod
    def generate(amount_of_batches=10, batch_size_from=50, batch_size_to=100):
        for i in range(0, amount_of_batches):
            users = list()
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f"Batch # {i} size {batch_size}")
            for _ in range(0, batch_size):
                users.append(GenerateRandomUser.generate_random())
            yield users
        sleep(5)
