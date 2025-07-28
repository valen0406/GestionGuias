from flask import Blueprint, request, jsonify
from models.instructor import Instructor

ruta_instructor = Blueprint('ruta_instructor', __name__)

@ruta_instructor.route('/api/instructores/', methods=['GET'])
def obtener_instructores():
    instructores = Instructor.objects()
    return jsonify(instructores), 200

@ruta_instructor.route('/api/instructor/', methods=['POST'])
def crear_instructor():
    data = request.get_json()
    nuevo = Instructor(**data)
    nuevo.save()
    return jsonify({"mensaje": "Instructor creado"}), 201

@ruta_instructor.route('/api/instructor/<id>/', methods=['PUT'])
def actualizar_instructor(id):
    data = request.get_json()
    instructor = Instructor.objects(id=id).first()
    if not instructor:
        return jsonify({"mensaje": "Instructor no encontrado"}), 404
    instructor.update(**data)
    return jsonify({"mensaje": "Instructor actualizado"}), 200

@ruta_instructor.route('/api/instructor/<id>/', methods=['DELETE'])
def eliminar_instructor(id):
    instructor = Instructor.objects(id=id).first()
    if not instructor:
        return jsonify({"mensaje": "Instructor no encontrado"}), 404
    instructor.delete()
    return jsonify({"mensaje": "Instructor eliminado"}), 200
