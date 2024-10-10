from kafka import KafkaConsumer
import pandas as pd
import json

consumer = KafkaConsumer(
    "titanic_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="titanic-group",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

processed_data = []

# – Maintain a count of the number of passengers processed, categorized by survival status (survived or did not survive).
survival_status = {
    "survived": 0,
    "did not survive": 0
}

def process_data(data):
    if validate_data(data):
        if data["Survived"] == 1:
            survival_status["survived"] += 1
        else:
            survival_status["did not survive"] += 1
        processed_data.append(data)
    #After processing the first 100 records, analyze the data.
    if len(processed_data) == 100:
        analyze_data()

#3. Data Analysis: 
def analyze_data():
        # The percentage of passengers who survived.
        percentage_survived = survival_status["survived"] / 100 * 100
        print(f"Percentage of passengers who survived: {percentage_survived}%")
        # – The average age of survivors vs. non-survivors.
        average_age_survivors = sum([data["Age"] for data in processed_data if data["Survived"] == 1]) / survival_status["survived"]
        average_age_non_survivors = sum([data["Age"] for data in processed_data if data["Survived"] == 0]) / survival_status["did not survive"]
        print(f"Average age of survivors: {average_age_survivors:.2f} years")
        print(f"Average age of non-survivors: {average_age_non_survivors:.2f} years")
        consumer.close()

def validate_data(data):
    required_keys =  ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    if all(key in data and pd.notna(data['Age']) for key in required_keys):
        # – Print the passenger name, class, and survival status.
        print(f"Valid data found: {data['Name']} - {data['Survived']} - {data['Pclass']}")
        return True
    # If a record has a missing value for any of the fields, log this information with a timestamp.
    print(f"Invalid data found: {data['timestamp']}")
    return False

try:
    while len(processed_data) < 100:
        for message in consumer:
            process_data(message.value)
except KeyboardInterrupt:
    print("Stopping consumer...")