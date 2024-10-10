import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import time
import json


def fetch_world_population():
    url = "https://www.worldometers.info/world-population/population-by-country/"
    response = requests.get(url)

    if response.status_code == 200:
        return parse_world_population(response)
    else:
        print("Request failed with status code", response.status_code)


def parse_world_population(resp):
    soup = BeautifulSoup(resp.text, "html.parser")

    # get Country Name, Population and Year of data
    table = soup.find("table", {"id": "example2"})
    rows = table.find_all("tr")
    data = []
    for row in rows[1:]:
        cols = row.find_all("td")
        country = cols[1].text
        population = cols[2].text
        year = cols[3].text
        data.append({'country': country, 'population': population, 'year': year})
    return data


def publish_world_population(data, delay):
    print("Publishing world population data to kafka")
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    for index, record in enumerate(data):
        print(f"Sending data: {record}")
        # print(f"Sending data: {[record["country"] , record["population"], record["year"]]}")
        producer.send("world_population", record)
        time.sleep(delay)
        # if index == 10:
        #     break

population_data = fetch_world_population()

publish_world_population(population_data, 5)
