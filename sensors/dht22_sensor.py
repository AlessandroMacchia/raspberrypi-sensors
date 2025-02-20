import adafruit_dht
import board
import pandas as pd
import time
import datetime


sensor = adafruit_dht.DHT22(board.D4)  # Crea il sensore


def read_dht22():
    try:
        time.sleep(2)  # Pausa per stabilizzare il sensore
        humidity = sensor.humidity
        temperature = sensor.temperature
        
        # Verifica se i dati sono validi (non None)
        if humidity is not None and temperature is not None:
            data = pd.DataFrame([{
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'temperature': temperature,
                'humidity': humidity
            }])
            print(data)
            return data
        else:
            raise RuntimeError("Valori di temperatura o umidità non validi")
    
    except RuntimeError as e:
        print(f"Errore durante la lettura del sensore DHT22: {e}")
        return pd.DataFrame()  # Ritorna un dataframe vuoto in caso di errore

if __name__ == "__main__":
    read_dht22()
