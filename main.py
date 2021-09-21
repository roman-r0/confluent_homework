from argparse import ArgumentParser

from entites.user import GenerateRandomUser
from generator.user_generator import UserGenerator
from producer.user_producer import UserProducer

from entites.product import GenerateRandomProduct
from generator.product_generator import ProductGenerator
from producer.product_producer import ProductProducer


def parse_command_line_args():
    arg_parser = ArgumentParser()

    # # Users
    # arg_parser.add_argument('--topic', required=False, default='user_raw_data', help='Topic name')
    # arg_parser.add_argument('--bootstrap-servers', required=False, default='localhost:9092',
    #                         help="Bootstrap server address")
    # arg_parser.add_argument('--schema-registry', required=False, default='http://localhost:8081',
    #                         help="Schema registry url")
    # arg_parser.add_argument('--schema-file', required=False, default='create-user-request.avsc',
    #                         help="Filename of Avro schema to use")

    # Products
    arg_parser.add_argument('--topic', required=False, default='products_raw_data', help='Topic name')
    arg_parser.add_argument('--bootstrap-servers', required=False, default='localhost:9092',
                            help="Bootstrap server address")
    arg_parser.add_argument('--schema-registry', required=False, default='http://localhost:8081',
                            help="Schema registry url")
    arg_parser.add_argument('--schema-file', required=False, default='create-product.avsc',
                            help="Filename of Avro schema to use")

    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_args()

    product_producer = ProductProducer(args)
    product = GenerateRandomProduct()

    for products in ProductGenerator.generate():
        product_producer.send_records(products)

    # user_producer = UserProducer(args)
    # user = GenerateRandomUser()

    # for users in UserGenerator.generate():
    #     user_producer.send_records(users)

