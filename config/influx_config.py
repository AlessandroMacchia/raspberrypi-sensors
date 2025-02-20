## **Configurazione di InfluxDB** (`config/influx_config.py`)
from dotenv import load_dotenv
import os

load_dotenv()

INFLUXDB_URL = "http://192.168.1.18:8086"
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = "GeneralProjects"
INFLUXDB_BUCKET = "sensor"