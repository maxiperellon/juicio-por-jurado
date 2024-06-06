from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import random
import os
import json

app = Flask(__name__)
app.config['DATA_FOLDER'] = 'data'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def importar_datos(filepath):
    datos = pd.read_excel(filepath)
    filas_como_dict = datos.to_dict(orient='records')
    lista_datos = []
    for fila in filas_como_dict:
        for dni, nombre in fila.items():
            lista_datos.append({"DNI": dni, "Nombre": nombre})
    return lista_datos

def seleccion(datos, num_titulares):
    if len(datos) < 16:
        print("El número de registros en los datos es menor a 16.")
    
    seleccionados = random.sample(datos, 16)
    titulares = seleccionados[:num_titulares]
    suplentes = seleccionados[num_titulares:]
    return titulares, suplentes

@app.route('/', methods=['GET', 'POST'])
def index():
    num_titulares = 12
    titulares, suplentes = [], []
    json_path = os.path.join(app.config['DATA_FOLDER'], 'alumnos.json')

    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['DATA_FOLDER'], filename)
            file.save(filepath)
            datos = importar_datos(filepath)
            try:
                titulares, suplentes = seleccion(datos, num_titulares)
                with open(json_path, 'w') as json_file:
                    json.dump({"titulares": titulares, "suplentes": suplentes}, json_file)
            except ValueError as e:
                return str(e)

    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            titulares = data['titulares']
            suplentes = data['suplentes']

    return render_template('index.html', titulares=titulares, suplentes=suplentes)

if __name__ == '__main__':
    if not os.path.exists(app.config['DATA_FOLDER']):
        os.makedirs(app.config['DATA_FOLDER'])
    app.run(debug=True)
