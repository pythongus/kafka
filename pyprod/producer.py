"""
Producer for the new_data.csv file
"""
import os
from sys import exit
from typing import Callable
from functools import partial
import logging
from kafka import KafkaProducer
from dotenv import load_dotenv
load_dotenv()


FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.WARNING)
SERVERS = os.getenv('SERVERS')
TOPIC = os.getenv('TOPIC')
DATA_FILE = os.getenv('DATA_FILE')


def run():
    if not SERVERS:
        LOGGER.error('SERVERS not set')
        exit(1)

    producer = KafkaProducer(bootstrap_servers=SERVERS)
    callback = partial(send, producer)
    get_data(callback)


def get_data(callback: Callable):
    if not DATA_FILE:
        LOGGER.error('DATA_FILE not set')
        exit(2)

    with open(DATA_FILE, 'r') as csv_input:
        while (line := csv_input.readline()):
            callback(line)


def send(producer: KafkaProducer, line: str):
    if not TOPIC:
        LOGGER.error('TOPIC not set')
        exit(3)

    producer.send(TOPIC, bytes(line.strip(), encoding='utf-8'))


if __name__ == '__main__':
    run()
