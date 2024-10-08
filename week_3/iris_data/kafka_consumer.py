from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer(
    "iris_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="iris-group",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

def process_data(data):
    print(f"Processing data: {data}")

try:
    for message in consumer:
        process_data(message.value)
except KeyboardInterrupt:
    print("Stopping consumer...")

consumer.close()