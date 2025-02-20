import RPi.GPIO as GPIO
import time
import pandas as pd

# Funzione per leggere lo stato del sensore di luce
def read_light_sensor(sensor_pin=22):
    # Configura la modalità di numerazione dei pin e il pin del sensore come input
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor_pin, GPIO.IN)

    try:
        # Legge lo stato del sensore
        if not GPIO.input(sensor_pin):
            luce=True
            data = pd.DataFrame([{
            'luce': luce,
        }])
            print(data)
            return data
        else:
            luce=False
            data = pd.DataFrame([{
            'luce': luce,
        }])
            print(data)
            return data
    except RuntimeError as e:
        print(f"Errore durante la lettura del sensore LM393: {e}")
        return pd.DataFrame()

    finally:
        GPIO.cleanup()  # Ripristina lo stato dei pin GPIO

# Main per eseguire la funzione
if __name__ == "__main__":
    read_light_sensor()  # Puoi passare un altro pin come parametro, se necessario
