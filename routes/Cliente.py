from flask import Blueprint, jsonify, request
from models.entities.Cliente import Cliente
from models.ClienteModel import ClienteModel



main = Blueprint('Cliente', __name__)


@main.route("/", methods=['GET'])
def get_Cliente():
    try:
        clientes = ClienteModel.getCliente()
        return jsonify(clientes)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500



@main.route("/add", methods=['POST'])
def add_Cliente():
    try:
        if request.json and 'Rut_Cliente' in request.json and 'Nombre' in request.json and 'Correo' in request.json and 'Contrasena' in request.json:
            cliente = Cliente(
                Rut_Cliente=request.json['Rut_Cliente'],
                Nombre=request.json['Nombre'],
                Correo=request.json['Correo'],
                Contrasena=request.json['Contrasena'])
            if ClienteModel.digito_verificador(cliente.Rut_Cliente):
              if ClienteModel.add_Cliente(cliente):
                return jsonify({"message": "Cliente agregado correctamente"})
              else:
                return jsonify({"message": "Error al agregar"}), 500
            else:
              return jsonify({"messaage": "Rut no valido"})
        else:
            return jsonify(
                {"message": "Required fields are missing in the request"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<Rut_Cliente>", methods=['DELETE'])
def delete_Cliente(Rut_Cliente):
    try:
        if ClienteModel.delete_Cliente(Rut_Cliente):
            return jsonify({"message": "Cliente eliminado correctamente"})
        else:
            return jsonify({"message": "El cliente no existe"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
        



@main.route('/login', methods=['POST'])
def login():
    try:
        if request.json and 'correo' in request.json and 'contrasena' in request.json:
            correo = request.json['correo']
            contrasena = request.json['contrasena']

            cliente = Cliente()
            cliente.Correo = correo
            cliente.Contrasena = contrasena

            if ClienteModel.login(cliente):
                return jsonify({"message": "Autenticación correcta"})
            else:
                return jsonify({"message": "Correo y/o contraseña incorrectos"}), 400
        else:
            return jsonify({"message": "Correo or contraseña key is missing in the request JSON"}), 400

    except Exception as ex:
        return jsonify({"message": str(ex)}), 400