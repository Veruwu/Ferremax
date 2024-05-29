from flask import Blueprint, jsonify, request
from models.ProductoModel import ProductoModel
from models.entities.Producto import Producto
#from models.entities.Producto import Producto

main = Blueprint("producto_blueprint", __name__)


@main.route("/")
def getProductos():
    try:
        productos = ProductoModel.getProducto()
        return jsonify(productos)
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500


@main.route("/cat/<ID_Categoria>")
def getProductosCat(ID_Categoria):
    try:
        productos = ProductoModel.getProductoCat(ID_Categoria)
        return jsonify(productos)
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500


@main.route("/add", methods=['POST'])
def add_Producto():
    try:
        if request.json and 'Nombre' in request.json and 'Descripcion' in request.json and 'Precio_Base' in request.json and 'ID_Categoria' in request.json and 'Fecha_Inicio_Estado' in request.json:
            producto = Producto(
                Nombre=request.json['Nombre'],
                Descripcion=request.json['Descripcion'],
                Precio_Base=request.json['Precio_Base'],
                ID_Categoria=request.json['ID_Categoria'],
                Fecha_Inicio_Estado=request.json['Fecha_Inicio_Estado'],
                )
            if ProductoModel.add_Producto(producto):
                return jsonify(producto.Nombre)
            else:
                return jsonify({"message": "Error al insertar"}), 500
        else:
            return jsonify(
                {"message": "Required fields are missing in the request"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@main.route("/update/<ID_Producto>", methods=['PUT'])
def update_Producto(ID_Producto):
    try:
        if request.json and 'Nombre' in request.json and 'Descripcion' in request.json and 'Precio_Base' in request.json and 'ID_Categoria' in request.json and 'Estado' in request.json and 'Fecha_Inicio_Estado' in request.json and 'Fecha_Fin_Estado' in request.json:
            producto = Producto(
                Nombre=request.json['Nombre'],
                Descripcion=request.json['Descripcion'],
                Precio_Base=request.json['Precio_Base'],
                ID_Categoria=request.json['ID_Categoria'],
                Estado=request.json['Estado'],
                Fecha_Inicio_Estado=request.json['Fecha_Inicio_Estado'],
                Fecha_Fin_Estado=request.json['Fecha_Fin_Estado'])
            if ProductoModel.update_Producto(producto, ID_Producto):
                return jsonify(producto.Nombre)
            else:
                return jsonify({"message": "Error al actualizar"}), 500
        else:
            return jsonify(
                {"message": "Required fields are missing in the request"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

    
