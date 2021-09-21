import json

from producer.base_producer import BaseProducer


class ProductProducer(BaseProducer):

    def __init__(self, args):
        super(ProductProducer, self).__init__(args)

    def send_record(self, key, value):
        self.producer.produce(topic=self.topic, key=key, value=value)

    def send_records(self, products):
        for product in products:
            self.send_record(key=product.name, value=product.to_json())
        self.producer.flush()
