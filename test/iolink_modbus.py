from pymodbus.client import ModbusTcpClient

# Configurar la IP del IO-Link Master
IO_LINK_IP = "192.168.0.13"  # Cambia por la IP real del IO-Link Master
MODBUS_PORT = 502  # Puerto estándar de Modbus TCP

# Dirección del registro Modbus del sensor en el IO-Link Master
REGISTER_ADDRESS = 1108  # Dirección del registro Modbus (depende del IO-Link Master)

# Crear cliente Modbus
client = ModbusTcpClient(IO_LINK_IP, port=MODBUS_PORT)

try:
    # Conectar al IO-Link Master
    if client.connect():
        print(f"Conectado a IO-Link Master en {IO_LINK_IP}")

        # Leer un registro de 16 bits desde el IO-Link Master
        response = client.read_holding_registers(REGISTER_ADDRESS, 1)

        if response.isError():
            print("Error al leer el registro")
        else:
            sensor_value = response.registers[0]
            print(f"Valor del sensor: {sensor_value}")

    else:
        print("No se pudo conectar al IO-Link Master")

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()  # Cerrar conexión
