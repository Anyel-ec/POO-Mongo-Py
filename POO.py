from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

class ManejadorPersona:
    def __init__(self, conexion_uri, db_name, collection_name):
        self.cliente = MongoClient(conexion_uri)
        self.db = self.cliente[db_name]
        self.collection = self.db[collection_name]

    def crear_persona(self, persona):
        persona_data = {
            'nombre': persona.nombre,
            'edad': persona.edad,
            'ocupacion': persona.ocupacion
        }
        result = self.collection.insert_one(persona_data)
        print(f"Persona creada con ID: {result.inserted_id}")

    def leer_persona(self, nombre):
        return self.collection.find_one({'nombre': nombre})

    def actualizar_persona(self, nombre, nuevos_datos):
        result = self.collection.update_one({'nombre': nombre}, {'$set': nuevos_datos})
        return result.modified_count > 0

    def eliminar_persona(self, nombre):
        result = self.collection.delete_one({'nombre': nombre})
        return result.deleted_count > 0

# Rutas de Flask
@app.route('/')
def index():
    estudiantes = manejador.collection.find()
    return render_template('index.html', estudiantes=estudiantes)

@app.route('/', methods=['POST'])
def crear_persona():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    ocupacion = request.form['ocupacion']

    nueva_persona = Persona(nombre, edad, ocupacion)
    manejador.crear_persona(nueva_persona)

    return redirect(url_for('index'))

@app.route('/editar/<nombre>', methods=['POST'])
def editar_persona(nombre):
    nuevos_datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido']
    }

    if manejador.actualizar_persona(nombre, nuevos_datos):
        return {'message': 'Persona actualizada exitosamente'}
    else:
        return {'message': 'Persona no encontrada'}, 404

@app.route('/eliminar/<nombre>', methods=['POST'])
def eliminar_persona(nombre):
    if manejador.eliminar_persona(nombre):
        return {'message': 'Persona eliminada exitosamente'}
    else:
        return {'message': 'Persona no encontrada'}, 404

if __name__ == '__main__':
    conexion_uri = "mongodb://localhost:27017/"
    db_name = "Prueba"
    collection_name = "personas"

    manejador = ManejadorPersona(conexion_uri, db_name, collection_name)

    app.run(debug=True)
