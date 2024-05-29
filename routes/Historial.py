from flask import Blueprint, jsonify, request
from models.HistorialModel import HistorialModel
from models.entities.Historial import Historial
#from models.entities.Producto import Producto


main = Blueprint("historial_blueprint", __name__)


@main.route("/")
def getHistoriales():
  try:
    historiales = HistorialModel.getHistorial()
    return jsonify(historiales)
  except Exception as ex:
    return jsonify({"msg": str(ex)}), 500


# @main.route("/add", methods=['POST'])
# def add_Historial():
#   try:
#     historial = historial(ID_HistorialPrecio =request.json['ID_HistorialPrecio'],
#                           ID_Producto =request.json['ID_Producto'],
#                           Precio_Anterior =request.json['Precio_Anterior'],
#                           Precio_Nuevo =request.json['Precio_Nuevo'],
#                           Fecha_Cambio =request.json['Fecha_Cambio'])
#     return jsonify({"message": "Product added successfully"}), 200
#   except Exception as ex:
#     return jsonify({"message": str(ex)}), 500