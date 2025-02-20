import os
import pandas as pd

def write_to_csv(data, filename="/home/alemacchia/Desktop/General_Experiments/project/data/pp·csv"):
    # Verifica se il file esiste
    file_exists = os.path.isfile(filename)
    
    # Apre il file in modalità append
    with open(filename, 'a') as file:
        # Se il file non esiste, scrive l'intestazione
        if not file_exists:
            data.to_csv(file, index=False, header=True)
        else:
            # Se il file esiste, scrive solo i dati senza l'intestazione
            data.to_csv(file, index=False, header=False)
