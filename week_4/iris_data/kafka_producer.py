import pandas as pd
from kafka import KafkaProducer
import time
import json

#import irish data
iris_data = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
    header=None,
    names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
)

producer = KafkaProducer(bootstrap_servers="localhost:9092" , value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def stream_iris_to_kafka(data, delay=1):
    for index, row in data.iterrows():
        producer.send('iris_data', value=row.to_dict())
        print(f"Sent data to Kafka: {row.to_dict()}")
        time.sleep(delay) 

stream_iris_to_kafka(iris_data, delay=1)

producer.close()