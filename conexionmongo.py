# Importar las bibliotecas necesarias
import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Si deseas utilizar seaborn para las gráficas
# import seaborn as sns

# Establecer la conexión con MongoDB
client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Elegir la base de datos y la colección que deseas utilizar
# (Reemplaza 'tu_base_de_datos' y 'tu_colección' con los nombres reales)
db = client['myDatabase']
collection = db['myCollection']

# Realizar una consulta para obtener todos los datos de la colección
# (o ajustar la consulta según tus necesidades)
data = collection.find()

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(list(data))

# Cerrar la conexión de cliente MongoDB
client.close()

# Asegúrate de que la columna que vas a graficar está en el formato correcto
# Por ejemplo, si es una fecha o un número, conviértelo al tipo de datos apropiado

# Realizar una gráfica (cambia 'campo_x' y 'campo_y' por los nombres de tus campos)
plt.figure(figsize=(10, 6))
plt.plot(df['campo_x'], df['campo_y'], marker='o')
plt.title('Título de la Gráfica')
plt.xlabel('Campo X')
plt.ylabel('Campo Y')
plt.grid(True)
plt.show()
