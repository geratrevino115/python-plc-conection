import pyads

# Configuración del PLC TwinCAT
PLC_IP = "192.168.0.55"  # Cambia esto por la IP del PLC
PLC_NET_ID = "5.45.231.63.1.1"  # NetID del PLC
AMS_PORT = 851  # Puerto AMS por defecto

# Crear conexión con el PLC
plc = pyads.Connection(PLC_NET_ID, AMS_PORT, PLC_IP)

try:
    plc.open()  # Abrir la conexión
    if plc.is_open:
        print("✅ Conexión establecida con TwinCAT")
        
        # Escribir en una variable booleana
        plc.write_by_name("MAIN.PBHMI2", False, pyads.PLCTYPE_BOOL)
        print("✅ Se escribió 'True' en 'MAIN.PBHMI2'")

        # Leer la variable para confirmar
        var_value = plc.read_by_name("MAIN.PBHMI1", pyads.PLCTYPE_BOOL)
        print(f"🔍 Valor actual de 'MAIN.PBHMI1': {var_value}")

except Exception as e:
    print(f"❌ Error en la conexión: {e}")

finally:
    plc.close()  # Cerrar conexión
    print("🔴 Conexión cerrada")
