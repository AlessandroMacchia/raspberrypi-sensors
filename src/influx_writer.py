import sys
from influxdb_client import InfluxDBClient, Point, WritePrecision
from config.influx_config import INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET
import pandas as pd
from influxdb_client.client.write_api import SYNCHRONOUS

def write_to_influx(df: pd.DataFrame):
    with InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        
        # Itera su ogni riga del DataFrame
        for index, row in df.iterrows():
            point = Point("sensor_data") \
                        .tag("location", "raspberrypi") \
                        .field("temperature", row['temperature']) \
                        .field("humidity", row['humidity']) \
                        .field("light", row['luce']) \
                        .time(row['timestamp'], WritePrecision.NS)
            
            write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

