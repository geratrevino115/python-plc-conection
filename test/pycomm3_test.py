from pycomm3 import LogixDriver

PLC_IP = "192.168.0.25"  # Cambia esto por la IP de tu PLC

def get_plc_tags(ip):
    try:
        with LogixDriver(ip) as plc:
            print(f"🔍 Buscando tags en el PLC {ip}...")
            tags = plc.get_tag_list()  # Obtener lista de tags
            
            if tags:
                print(f"✅ Tags encontrados en {ip}:")
                print("📜 Estructura de los datos recibidos:")
                print(tags)  # 🔍 Esto nos ayudará a entender cómo se devuelven los datos

                # Intentamos acceder a los tags según su estructura real
                for tag in tags:
                    print(tag)  # 🔍 Imprime cada objeto tag para verificar su estructura

            else:
                print(f"❌ No se encontraron tags en el PLC {ip}")

    except Exception as e:
        print(f"❌ Error al conectar con el PLC: {e}")

# Ejecutar la función
get_plc_tags(PLC_IP)
