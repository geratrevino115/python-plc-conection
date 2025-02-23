import requests

IOLINK_MASTER_IP = "192.168.0.13"  # ⚡ Cambia por la IP de tu IO-Link Master
URL = f"http://{IOLINK_MASTER_IP}/api/v1/modules"  # Endpoint de la API

def check_io_link_api():
    try:
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()  # Convertir respuesta a JSON
            print("✅ Respuesta completa del IO-Link Master:")
            print(data)  # 🔍 Imprime la estructura real del JSON

        else:
            print(f"❌ Error HTTP {response.status_code}: {response.text}")

    except Exception as e:
        print(f"❌ Error de conexión: {e}")

# Ejecutar la función para ver la respuesta de la API
check_io_link_api()

