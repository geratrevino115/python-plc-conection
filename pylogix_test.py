from pylogix import PLC

# Configura la IP del PLC
PLC_IP = "192.168.0.25"  # ⚡ Cambia esto por la IP real de tu PLC

def get_plc_tags(ip):
    with PLC() as comm:
        comm.IPAddress = ip  # Configurar IP del PLC
        
        print(f"🔍 Buscando tags en el PLC {ip}...")
        response = comm.GetTagList()  # Obtener lista de tags
        
        if response.Status == "Success":
            print(f"✅ Tags encontrados en {ip}:")
            for tag in response.Value:
                print(f"📌 {tag.TagName} - Tipo: {tag.DataType}")
        else:
            print(f"❌ No se pudo obtener la lista de tags: {response.Status}")

# Ejecutar la función
get_plc_tags(PLC_IP)

#Escribir en un tag
def write_tag(ip, tag, value):
    with PLC() as comm:
        comm.IPAddress = ip  # Configurar IP del PLC
        
        print(f"📝 Escribiendo valor {value} en el tag {tag} del PLC {ip}...")
        response = comm.Write(tag, value)  # Escribir en el tag
        
        if response.Status == "Success":
            print(f"✅ Escritura exitosa en el tag {tag}")
        else:
            print(f"❌ Error al escribir en el tag {tag}: {response.Status}")

# Ejecutar la función
write_tag(PLC_IP, "Program:MainProgram.PBHMI1", 0)  # Cambiar por el tag y el valor deseados

#Leer un tag
def read_tag(ip, tag):
    with PLC() as comm:
        comm.IPAddress = ip  # Configurar IP del PLC
        
        print(f"🔍 Leyendo valor del tag {tag} en el PLC {ip}...")
        response = comm.Read(tag)  # Leer el tag
        
        if response.Status == "Success":
            print(f"✅ Valor leído del tag {tag}: {response.Value}")
        else:
            print(f"❌ Error al leer el tag {tag}: {response.Status}")

# Ejecutar la función
read_tag(PLC_IP, "Program:MainProgram.PBHMI2")  # Cambiar por el tag deseado