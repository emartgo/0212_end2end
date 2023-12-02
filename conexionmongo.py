# Importar las bibliotecas necesarias
import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Establecer la conexión con MongoDB
client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Elegir la base de datos y la colección que deseas utilizar
db = client['myDatabase']  # Asegúrate de que 'myDatabase' es el nombre real de tu base de datos
collection = db['myCollection']  # Asegúrate de que 'myCollection' es el nombre real de tu colección

# Realizar una consulta para obtener los campos 'address' y 'available' de todos los documentos
data = collection.find({}, {'address': 1, 'available': 1, '_id': 0})

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(list(data))

# Cerrar la conexión de cliente MongoDB
client.close()

# Asegúrate de que la columna 'available' esté en el formato correcto (numérico)
df['available'] = pd.to_numeric(df['available'], errors='coerce')
df.dropna(subset=['available'], inplace=True)  # Eliminar filas con valores no numéricos o faltantes

# Ordenar el DataFrame por la cantidad de bicicletas disponibles para mejor visualización
df.sort_values(by='available', ascending=True, inplace=True)

# Crear un gráfico de barras
plt.figure(figsize=(10, 8))
plt.barh(df['address'], df['available'])  # Gráfico de barras horizontal
plt.xlabel('Cantidad de Bicicletas Disponibles')
plt.title('Disponibilidad de Bicicletas por Dirección')
plt.gca().invert_yaxis()  # Invertir el eje Y para mostrar la barra más alta en la parte superior
plt.tight_layout()  # Ajustar la disposición para que todo encaje bien en el gráfico
plt.show()
