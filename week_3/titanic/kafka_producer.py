import pandas as pd
from kafka import KafkaProducer
import time
import json

titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

procedure = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def stream_titanic_to_kafka(data, delay=0.5):
    for _, row in data.iterrows():
        procedure.send('titanic_data', value=row.to_dict())
        print(f"Sent data to Kafka: {row.to_dict()}")
        time.sleep(delay)

stream_titanic_to_kafka(titanic_data, delay=0.5)

procedure.close()