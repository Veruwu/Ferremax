from flask import Blueprint, jsonify, request
from models.InventarioModel import InventarioModel
from models.entities.Inventario import Inventario

main = Blueprint('Inventario', __name__)

@main.route('/')
def get_Inventario():
  try:
    inventario = InventarioModel.getInventario()
    return jsonify(inventario)
  except Exception as ex:
    return jsonify({"msg": str(ex)}), 500