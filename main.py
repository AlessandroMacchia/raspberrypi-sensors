import sys
import os
from sensors.dht22_sensor import read_dht22
from sensors.lm393_photosensitive import read_light_sensor
from src.csv_writer import write_to_csv
from src.influx_writer import write_to_influx
import time
import datetime
import pandas as pd

#just for commit

for _ in range(10):

    data_dht22 = read_dht22()  # Leggi i dati dal sensore
    print(data_dht22)
    time.sleep(10)
    data_lm393= read_light_sensor()
    combined_df = pd.concat([data_dht22, data_lm393], axis=1)
    combined_df["timestamp"]= datetime.datetime.utcnow().isoformat()  # Aggiungi timestamp
    write_to_csv(combined_df)  # Scrivi i dati nel CSV
    write_to_influx(combined_df)  # Scrivi i dati in InfluxDB
    time.sleep(10)
