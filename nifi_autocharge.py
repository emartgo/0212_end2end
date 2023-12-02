import requests
import time

# Espera a que NiFi esté listo
time.sleep(30)

# Carga el flujo de trabajo
url = "http://localhost:8443/nifi-api/process-groups/root/templates/upload"
files = {'template': open('nifi/flow.xml', 'rb')}
response = requests.post(url, files=files, verify=False)

# Comprueba si la carga fue exitosa
if response.status_code == 201:
    print("Flujo de trabajo cargado con éxito.")
else:
    print("Error al cargar el flujo de trabajo.")
    print(response.text)
    print(response.status_code)