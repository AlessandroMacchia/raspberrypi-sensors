import adafruit_dht
import board
import pandas as pd
import time
import datetime
from pymodbus.client import ModbusTcpClient

sensor = adafruit_dht.DHT22(board.D4)  # Crea il sensore

# Configura il client Modbus
MODBUS_SERVER_IP = "192.168.1.18"  # Cambia con l'IP del Raspberry se necessario
MODBUS_PORT = 5020
client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_PORT)

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
            return temperature, humidity
        else:
            raise RuntimeError("Valori di temperatura o umidità non validi")
    
    except RuntimeError as e:
        print(f"Errore durante la lettura del sensore DHT22: {e}")
        return None, None  # Ritorna None in caso di errore

def send_to_modbus(temperature, humidity):
    # Converte i valori in interi per Modbus
    temp_int = int(temperature * 10)  # es. 25.3°C -> 253
    hum_int = int(humidity * 10)  # es. 60.2% -> 602
    
    try:
        # Scrive i dati nei registri Modbus
        if client.connect():
            print(f"✅ Connessione a {MODBUS_SERVER_IP} riuscita")
            client.write_register(0, temp_int)  # Registro 0 = Temperatura
            client.write_register(1, hum_int)  # Registro 1 = Umidità
            print(f"Dati inviati correttamente: temp = {temp_int}, umidità = {hum_int}")
            client.close()  # Chiude la connessione
        else:
            print("❌ Connessione al server Modbus fallita.")
    except Exception as e:
        print(f"Errore durante l'invio dei dati al server Modbus: {e}")

if __name__ == "__main__":
    while True:
        temperature, humidity = read_dht22()
        
        if temperature is not None and humidity is not None:
            send_to_modbus(temperature, humidity)
        
        time.sleep(5)  # Aspetta 5 secondi prima della prossima lettura
