# Juicio por Jurado

Esta es una aplicación web para seleccionar jurados titulares y suplentes a partir de un archivo Excel. La aplicación está construida con Flask y permite cargar un archivo Excel para generar una lista de jurados aleatoria y almacenarla en un archivo JSON.

## Características

- Carga de archivos Excel para importar datos de jurados.
- Selección aleatoria de jurados titulares y suplentes.
- Almacenamiento de la selección en un archivo JSON.
- Interfaz web amigable para cargar archivos y ver los resultados.

## Requisitos Previos

- Python 3.6 o superior.
- pip (gestor de paquetes de Python).

## Instalación

Siga estos pasos para instalar y ejecutar la aplicación en su entorno local:

### 1. Clonar el Repositorio

Primero, clone el repositorio en su máquina local:

```bash
git clone https://github.com/maxiperellon/juicio-por-jurado.git
```
```bash
cd juicio-por-jurado
```

### 2. Crear y Activar un Entorno Virtual

Cree un entorno virtual para gestionar las dependencias de Python:

```bash
python -m venv venv
```

Active el entorno virtual. El comando para activar el entorno virtual depende de su sistema operativo:

* Windows:
```bash
.\venv\Scripts\activate
```
* macOS / Linux:
```bash
source venv/bin/activate
```  

### 3. Instalar las Dependencias

Con el entorno virtual activado, instale las dependencias del proyecto:
```bash
pip install -r requirements.txt
``` 
### 4. Ejecutar la Aplicación

Inicie la aplicación Flask:
```bash
python app.py
```
o
```bash
python3 app.py
```
La aplicación estará disponible en http://127.0.0.1:5000 o http://localhost:5000. Abra cualquiera de estos enlaces en su navegador web.

## Uso

### Cargar un Archivo Excel

1. Acceda a la interfaz web.
2. Use el botón "Seleccionar archivo Excel" para cargar su archivo Excel.
3. Haga clic en "Cargar y Seleccionar" para procesar el archivo y ver los jurados seleccionados.

### Estructura de Archivos

* `app.py`: Contiene la lógica principal de la aplicación Flask.
* `templates/index.html`: La plantilla HTML para la interfaz web.
* `static/styles.css`: Archivo CSS para el estilo de la interfaz.
* `data/alumnos.json`: Archivo JSON donde se guarda la lista de jurados seleccionados.

## Detalles Técnicos

### Configuración de Flask

- **DATA_FOLDER**: Carpeta `data` donde se guarda el archivo JSON con los jurados seleccionados.

### Funciones Principales

`archivo_permitido(nombre_archivo)`

Verifica si un archivo tiene una extensión permitida.

Argumento: 
* `nombre_archivo` (str) - Nombre del archivo a verificar.

Devuelve: 
* `bool` - `True` si la extensión está permitida, `False` en caso contrario.

`importar_datos(filepath)`

Importa datos desde un archivo Excel y los convierte en una lista de diccionarios.

Argumento: 
* `filepath` (str) - Ruta al archivo Excel.

Devuelve: 
* `lista_datos` - Lista de diccionarios con los datos de los jurados.

`seleccion(datos, alumnos_random, num_titulares)`

Selecciona un número aleatorio de alumnos como titulares y suplentes.

Argumentos:

* `datos` (list): Lista de diccionarios con los datos de los jurados.
* `alumnos_random` (int): Número total de alumnos a seleccionar.
* `num_titulares` (int): Número de titulares a seleccionar.

Devuelve:

* `titulares` (list): Lista de jurados titulares.
* `suplentes` (list): Lista de jurados suplentes.

## Realizado Por

Este proyecto fue realizado por alumnos de quinto año de informática 2024 del Colegio del Carmen:

- ALVAREZ VARGAS, AUGUSTO
- ARIAS, FERNANDO JEREMIAS
- BERNABE VELILLA, JUAN PABLO
- BUCHTER, JOAQUIN SEBASTIAN
- CALVO DEMURU, VALENTINO HUGO
- CASANOVA, JUAN MARCO
- DUBROWSKY, EZEQUIEL
- GARRIDO, AGUSTÍN
- GATICA SOSA, LUCIANO BENJAMÍN
- GIORDANO, TADEO
- GOMEZ HERNANDEZ, MÁXIMO
- MANCHADO, JUAN IGNACIO
- MATARAZZO MATOZ, CHIARA ADRIANA
- MAZZAMATI , JUAN PABLO
- MOYANO YAÑEZ, FACUNDO NICOLÁS
- OLMEDO, LUCIANO FRANCISCO

**¡Gracias por su contribución!**

### Guiado por:
* **[Maximiliano A. Perellón](https://github.com/maxiperellon)**


