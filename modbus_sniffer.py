from scapy.all import sniff, IP, TCP, Raw

def packet_callback(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 5020:  # Solo pacchetti sulla porta 5020
        print(f"\n📡 Pacchetto Modbus TCP intercettato da {packet[IP].src} a {packet[IP].dst}")
        
        if packet.haslayer(Raw):  # Se il pacchetto contiene dati Modbus
            data = packet[Raw].load.hex()  # Converti in esadecimale
            print(f"📜 Dati Modbus (in chiaro): {data}")
            # Decodifica il pacchetto per estrarre valori di temperatura e umidità
            if len(data) >= 12:
                temp = int(data[8:12], 16) / 10  # Temperatura in formato decimale
                hum = int(data[12:16], 16) / 10  # Umidità in formato decimale
                print(f"🌡️ Temperatura: {temp}°C, Umidità: {hum}%")

# Avvia lo sniffing sulla rete
print("🔍 In ascolto sui pacchetti Modbus TCP...")
sniff(filter="tcp port 5020", prn=packet_callback, store=0)
