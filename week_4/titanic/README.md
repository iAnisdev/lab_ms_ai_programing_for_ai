# Iris Data Streaming with Kafka and Python

This project demonstrates how to stream and process the Iris dataset using Apache Kafka and Python. Follow the instructions below to set up your environment and run the application.

## Prerequisites

Before proceeding, ensure you have the following set up:

- **Python**: Install Python from [python.org](https://www.python.org/downloads/).
- **Apache Kafka**: Install Apache Kafka from the [official website](https://kafka.apache.org/downloads).
  ```bash
  brew install kafka
  ```
- **Run kafka server**:

  ```bash
    brew services start zookeeper
    brew services start kafka
  ```

- **Kafka-Python and Pandas Libraries**: Install the required Python libraries using pip:
  ```bash
  pip install kafka-python pandas
  ```

- **Create a Kafka topic named titanic data**

  ```bash
  kafka-topics --create --topic titanic-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  ```
