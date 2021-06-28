"""
Consumer client for Kafka
"""
import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()


TOPIC = os.getenv('TOPIC')
SERVERS = os.getenv('SERVERS')
CONSUMER_GROUP = os.getenv('CONSUMER_GROUP')


def run():
    consumer = KafkaConsumer(
        TOPIC, bootstrap_servers=SERVERS, group_id=CONSUMER_GROUP)
    try:
        for message in consumer:
            print(message.value.decode())
    except KeyboardInterrupt:
        print('Consumer finished by user')


if __name__ == '__main__':
    run()
