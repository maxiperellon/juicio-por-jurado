from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import random
import os
import json

app = Flask(__name__)
app.config['DATA_FOLDER'] = 'data'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

# Función para verificar si el archivo es permitido.
def archivo_permitido(nombre_archivo):
    # Verifica que el nombre del archivo tenga un punto y una extensión.
    if '.' not in nombre_archivo:
        return False
    
    # Extrae la extensión del archivo y la convierte a minúsculas.
    extension = nombre_archivo.rsplit('.', 1)[1].lower()
    
    # Verifica si la extensión está en la lista de extensiones permitidas.
    return extension in app.config['ALLOWED_EXTENSIONS']

# Función para importar datos desde un archivo Excel.
def importar_datos(filepath):
    datos = pd.read_excel(filepath)
    filas_como_dict = datos.to_dict(orient='records')
    lista_datos = []
    for fila in filas_como_dict:
        for dni, nombre in fila.items():
            lista_datos.append({"DNI": dni, "Nombre": nombre})
    return lista_datos

# Función para seleccionar titulares y suplentes.
def seleccion(datos, alumnos_random, num_titulares):
    if len(datos) < alumnos_random:
        print(f"El número de registros en los datos es menor a { alumnos_random }.")
        return [], []
    
    seleccionados = random.sample(datos, alumnos_random)
    titulares = seleccionados[:num_titulares]
    suplentes = seleccionados[num_titulares:]
    return titulares, suplentes

# Ruta principal para cargar y mostrar datos.
@app.route('/', methods=['GET', 'POST'])
def index():
    alumnos_random = 16
    num_titulares = 12
    titulares, suplentes = [], []
    json_path = os.path.join(app.config['DATA_FOLDER'], 'alumnos.json')

    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No hay archivo en la solicitud'
        file = request.files['file']
        if file.filename == '':
            return 'No se seleccionó ningún archivo'
        if file and archivo_permitido(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['DATA_FOLDER'], filename)
            file.save(filepath)
            datos = importar_datos(filepath)
            try:
                titulares, suplentes = seleccion(datos, alumnos_random, num_titulares)
                with open(json_path, 'w') as json_file:
                    json.dump({"titulares": titulares, "suplentes": suplentes}, json_file)
            except ValueError as e:
                return str(e)
            
    # Carga datos del archivo JSON si existe.
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            titulares = data['titulares']
            suplentes = data['suplentes']

    return render_template('index.html', titulares=titulares, suplentes=suplentes)

if __name__ == '__main__':
    app.run(debug=True)
