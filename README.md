# Conexión a PLCs con Python

Este repositorio contiene ejemplos de conexión con distintos PLCs utilizando Python. Se incluyen scripts para comunicarse con:

- **Allen-Bradley** usando `pylogix`
- **Siemens** usando `snap7`
- **Beckhoff (TwinCAT)** usando `pyads`

---

## 🚀 **Instalación y Requisitos**
Antes de ejecutar los scripts, instala las dependencias necesarias:

```bash
pip install pylogix python-snap7 pyads
```

Si trabajas con Siemens, es posible que necesites instalar **Snap7** manualmente desde:
🔗 [https://sourceforge.net/projects/snap7/](https://sourceforge.net/projects/snap7/)

---

## 🔌 **Conexión con Allen-Bradley (pylogix)**
📌 **Archivo:** `allen_bradley.py`

### **Ejemplo de conexión**
```python
from pylogix import PLC

plc = PLC()
plc.IPAddress = "192.168.1.10"  # Cambia a la IP de tu PLC

# Leer una variable
response = plc.Read("TagName")
print(f"Valor leído: {response.Value}")

# Escribir en una variable
plc.Write("TagName", 1)

plc.Close()
```
🛠 **Asegúrate de:**
- Tener la IP correcta del PLC.
- Usar el nombre exacto del tag en el PLC.

---

## ⚙️ **Conexión con Siemens (snap7)**
📌 **Archivo:** `siemens.py`

### **Ejemplo de conexión**
```python
import snap7
from snap7.util import get_int

plc = snap7.client.Client()
plc.connect("192.168.1.20", 0, 1)  # IP del PLC, Rack, Slot

# Leer un área de memoria (DB1, offset 0, tamaño 2 bytes)
data = plc.read_area(snap7.type.Areas.DB, 1, 0, 2)
value = get_int(data, 0)
print(f"Valor leído: {value}")

plc.disconnect()
```
🛠 **Consideraciones:**
- Verifica el **Rack y Slot** en **Siemens TIA Portal**.
- Asegura que la conexión está habilitada en el PLC.

---

## 🖥️ **Conexión con Beckhoff TwinCAT (pyads)**
📌 **Archivo:** `beckhoff.py`

### **Ejemplo de conexión**
```python
import pyads

PLC_IP = "192.168.0.55"
PLC_NET_ID = "5.45.231.63.1.1"
AMS_PORT = 851

plc = pyads.Connection(PLC_NET_ID, AMS_PORT, PLC_IP)
plc.open()

if plc.is_open:
    print("Conexión establecida con TwinCAT")

    # Leer un valor
    value = plc.read_by_name("MAIN.PBHMI1", pyads.PLCTYPE_BOOL)
    print(f"Valor de 'PBHMI1': {value}")

    # Escribir un valor
    plc.write_by_name("MAIN.PBHMI1", True, pyads.PLCTYPE_BOOL)

plc.close()
```
🛠 **Para Beckhoff:**
- Agrega la PC al **AMS Router** en TwinCAT.
- Verifica el **NetID** y la **IP** del PLC.
- Asegura que TwinCAT está en **RUN Mode**.

---

## 📝 **Contribuciones**
Si deseas mejorar este repositorio, ¡eres bienvenido! Puedes hacer un **fork**, enviar un **pull request** o reportar problemas en la sección de **issues**.

---

## 📜 **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
