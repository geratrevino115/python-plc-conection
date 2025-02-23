from opcua import Client

# Configura la IP del IO-Link Master y el puerto OPC UA
IOLINK_MASTER_IP = "192.168.0.55"  # ⚡ Cambia esto por la IP real de tu IO-Link Master
OPC_SERVER_URL = f"opc.tcp://{IOLINK_MASTER_IP}:851"

def get_opcua_sensors():
    try:
        # Conectar al servidor OPC UA
        client = Client(OPC_SERVER_URL)
        client.connect()
        print(f"✅ Conectado al servidor OPC UA en {OPC_SERVER_URL}")

        # 🔍 Explorar el servidor para ver los nodos disponibles
        root = client.get_root_node()
        print(f"🌳 Nodo raíz del servidor OPC UA: {root}")

        # 🔍 Obtener los objetos disponibles en el servidor
        objects = client.get_objects_node()
        print(f"📦 Objetos disponibles en el servidor: {objects.get_children()}")

        client.disconnect()

    except Exception as e:
        print(f"❌ Error al conectar con OPC UA: {e}")

# Ejecutar la función
get_opcua_sensors()
