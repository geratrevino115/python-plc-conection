import snap7
from snap7.util import set_bool
from snap7.util import get_bool

# 📡 Configuración del PLC Siemens
PLC_IP = "192.168.0.8"  # ⚡ Cambia esto por la IP real del PLC
RACK = 0  # S7-1200/1500 → 0, S7-300/400 → 0
SLOT = 2  # S7-1200/1500 → 1, S7-300/400 → 2
MEMORY_BYTE = 0  # Byte en memoria (M0)
BIT_INDEX = 0  # Bit dentro del byte (M0.0)
VALUE = False  # Valor a escribir (True o False)

def write_memory_bit(ip, rack, slot, byte, bit, value):
    """Escribe un BOOL en la memoria de marca (M)"""
    plc = snap7.client.Client()
    plc.connect(ip, rack, slot)

    if not plc.get_connected():
        print("❌ No se pudo conectar al PLC")
        return

    # Leer el byte completo donde está M0.0
    data = plc.read_area(snap7.type.Areas.MK, 0, byte, 1)

    # Modificar solo el bit necesario
    set_bool(data, 0, bit, value)

    # Escribir el byte modificado de vuelta en la memoria del PLC
    plc.write_area(snap7.type.Areas.MK, 0, byte, data)

    plc.disconnect()
    print(f"✅ Escrito {value} en M{byte}.{bit}")

# 🔥 Escribir en M0.0
write_memory_bit(PLC_IP, RACK, SLOT, MEMORY_BYTE, BIT_INDEX, VALUE)



OUTPUT_BYTE = 0  # Byte de salida (Q0)
BIT_INDEX = 0  # Bit dentro del byte (Q0.1)

def read_output_bit(ip, rack, slot, byte, bit):
    """Lee el estado de una salida digital (Q)"""
    plc = snap7.client.Client()
    plc.connect(ip, rack, slot)

    if not plc.get_connected():
        print("❌ No se pudo conectar al PLC")
        return None

    # Leer el byte completo de salidas
    data = plc.read_area(snap7.type.Areas.PA, 0, byte, 1)

    # Obtener solo el bit específico (Q0.1)
    value = get_bool(data, 0, bit)

    plc.disconnect()
    return value

# 🔥 Leer estado de Q0.1
q01_value = read_output_bit(PLC_IP, RACK, SLOT, OUTPUT_BYTE, BIT_INDEX)

print(f"📊 Estado de Q0.0: {q01_value}")
