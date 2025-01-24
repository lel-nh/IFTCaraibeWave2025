import csv
import random
from datetime import datetime, timedelta
import time

# Sensor definitions: fixed values for Start, Latitude, Longitude, and Code
sensors = [
    {"Start": "S", "Latitude": 16.2659, "Longitude": -60.924, "Code": "Z46MH"},
    {"Start": "S", "Latitude": 16.0186, "Longitude": -62.1204, "Code": "N12NY"},
    {"Start": "S", "Latitude": 15.8964, "Longitude": -60.5246, "Code": "L89CA"},
    {"Start": "S", "Latitude": 16.4265, "Longitude": -60.9873, "Code": "L56LD"},
    {"Start": "S", "Latitude": 16.3249, "Longitude": -60.412, "Code": "T78TK"},
    {"Start": "S", "Latitude": 16.5262, "Longitude": -61.5054, "Code": "A12BC"},
    {"Start": "S", "Latitude": 16.3482, "Longitude": -61.3523, "Code": "C34DE"},
    {"Start": "S", "Latitude": 16.028, "Longitude": -61.0179, "Code": "E56FG"},
    {"Start": "S", "Latitude": 15.8025, "Longitude": -61.2563, "Code": "G78HI"},
    {"Start": "S", "Latitude": 16.2786, "Longitude": -61.8247, "Code": "I90JK"},
    {"Start": "S", "Latitude": 16.421, "Longitude": -61.824, "Code": "K12LM"},
    {"Start": "S", "Latitude": 15.9038, "Longitude": -60.8042, "Code": "M34NO"},
    {"Start": "S", "Latitude": 16.642, "Longitude": -61.4425, "Code": "O56PQ"},
    {"Start": "S", "Latitude": 16.1406, "Longitude": -61.9782, "Code": "Q78RS"},
    {"Start": "S", "Latitude": 16.3736, "Longitude": -60.9356, "Code": "S90TU"},
    {"Start": "S", "Latitude": 15.7487, "Longitude": -61.154, "Code": "U12VW"},
    {"Start": "S", "Latitude": 16.7257, "Longitude": -61.6404, "Code": "W34XY"},
    {"Start": "S", "Latitude": 16.1626, "Longitude": -61.3536, "Code": "Y56ZA"},
    {"Start": "S", "Latitude": 16.0002, "Longitude": -61.2785, "Code": "B78CD"},
    {"Start": "S", "Latitude": 16.8156, "Longitude": -61.5402, "Code": "D90EF"}
]

# File name
csv_file = "sensors.csv"

# Function to generate a random number between 30 and 50
def generate_random_number():
    return random.randint(30, 50)

# Function to write the latest data for all sensors
def write_latest_data():
    # Current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        # Write a line for each sensor
        for sensor in sensors:
            row = [
                sensor["Start"],
                sensor["Latitude"],
                sensor["Longitude"],
                sensor["Code"],
                generate_random_number(),
                timestamp
            ]
            writer.writerow(row)

# Simulate data generation every minute
if __name__ == "__main__":
    print("Starting sensor data generation. Press Ctrl+C to stop.")
    try:
        while True:
            write_latest_data()
            print(f"Latest data written to {csv_file}.")
            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("Data generation stopped.")
