from flask import Blueprint, jsonify, request
from models.entities.Consulta import Consulta
from models.MensajeModel import MensajesModel

main = Blueprint('Consulta', __name__)

@main.route('/add/<Rut_Cliente>', methods=['POST'])
def addMensaje(Rut_Cliente):
    try:
        if request.json and 'Mensaje' in request.json:
            consulta = Consulta(
                Mensaje=request.json['Mensaje'])
            if MensajesModel.add_Mensaje(consulta, Rut_Cliente):
                return jsonify({"message": "Mensaje enviado correctamente"})
            else:
                return jsonify({"message": "Error al enviar"}), 500
        else:
            return jsonify(
                {"message": "Required fields are missing in the request"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@main.route('/get/<Rut_Cliente>', methods=['GET'])
def getMensaje(Rut_Cliente):
    try:
        clientes = MensajesModel.get_Mensaje(Rut_Cliente)
        return jsonify(clientes)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
