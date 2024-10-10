from kafka import KafkaConsumer
import pandas as pd


consumer = KafkaConsumer(
    "world_population",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="world_population_group"
)

data = []

for record in consumer:
    print(record.value)
    # data.append(record.value)
    

df = pd.DataFrame(data)
print(df)