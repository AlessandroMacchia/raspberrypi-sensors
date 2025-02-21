from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import signal
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
# Creiamo un blocco di memoria Modbus con 10 registri inizializzati a 0
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 10),  # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0] * 10),  # Coils
    hr=ModbusSequentialDataBlock(0, [0] * 10),  # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0] * 10),  # Input Registers
)

context = ModbusServerContext(slaves=store, single=True)

# Funzione per gestire l'interruzione del server
def signal_handler(sig, frame):
    print("❌ Server fermato.")
    sys.exit(0)

# Gestiamo il segnale di interruzione (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Avvio del server
try:
    print("📡 Avvio server Modbus TCP sulla porta 5020...")
    StartTcpServer(context, address=("0.0.0.0", 5020))
except Exception as e:
    print(f"❌ Errore durante l'avvio del server: {e}")
