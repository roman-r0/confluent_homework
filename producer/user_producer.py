import json

from producer.base_producer import BaseProducer


class UserProducer(BaseProducer):

    def __init__(self, args):
        super(UserProducer, self).__init__(args)

    def send_record(self, key, value):
        self.producer.produce(topic=self.topic, key=key, value=value)

    def send_records(self, users):
        for user in users:
            self.send_record(key=user.email, value=user.to_json())
        self.producer.flush()
