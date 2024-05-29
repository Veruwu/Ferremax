from flask import Blueprint, jsonify, request

from models.VendedorModel import VendedorModel
from models.entities.Vendedor import Vendedor

main = Blueprint('Vendedor', __name__)

@main.route("/", methods=['GET'])
def get_Vendedor():
    try:
        vendedores = VendedorModel.getVendedor()
        return jsonify(vendedores)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500



@main.route("/add", methods=['POST'])
def add_Vendedor():
    try:
        if request.json and 'Rut_Vendedor' in request.json and 'Nombre' in request.json and 'Correo' in request.json and 'Contrasena' in request.json:
            vendedor = Vendedor(
                Rut_Vendedor=request.json['Rut_Vendedor'],
                Nombre=request.json['Nombre'],
                Correo=request.json['Correo'],
                Contrasena=request.json['Contrasena'])
            if VendedorModel.digito_verificador(vendedor.Rut_Vendedor):
              if VendedorModel.add_Vendedor(vendedor):
                return jsonify({"message": "Vendedor agregado correctamente"})
              else:
                return jsonify({"message": "Error al agregar"}), 500
            else:
              return jsonify({"messaage": "Rut no valido"})
        else:
            return jsonify(
                {"message": "Required fields are missing in the request"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route('/login', methods=['POST'])
def login():
    try:
        if request.json and 'correo' in request.json and 'contrasena' in request.json:
            correo = request.json['correo']
            contrasena = request.json['contrasena']

            vendedor = Vendedor()
            vendedor.Correo = correo
            vendedor.Contrasena = contrasena

            if VendedorModel.login(vendedor):
                return jsonify({"message": "Autenticación correcta"})
            else:
                return jsonify({"message": "Correo y/o contraseña incorrectos"}), 500
        else:
            return jsonify({"message": "Correo or contraseña key is missing in the request JSON"}), 400

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500