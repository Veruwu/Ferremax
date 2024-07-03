
from flask import request, jsonify, Blueprint
import requests

main = Blueprint("Moneda", __name__)


API_KEY = '53733|Lby5wPoJyWOY0LMb24Qc'
CAMBIO_TODAY_API_URL = 'https://api.cambio.today/v1/quotes/{from_currency}/{to_currency}/json?quantity={amount}&key={api_key}'

@main.route('/convertir_monedas', methods=['POST'])
def convertir_monedas():
    data = request.json

    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    cantidad = data.get('cantidad')
    if cantidad is None:
        return jsonify({'error': 'Missing cantidad in request'}), 400

    moneda_origen = data.get('moneda_origen')
    if moneda_origen is None:
        return jsonify({'error': 'Missing moneda_origen in request'}), 400

    moneda_destino = data.get('moneda_destino')
    if moneda_destino is None:
        return jsonify({'error': 'Missing moneda_destino in request'}), 400

    url = CAMBIO_TODAY_API_URL.format(from_currency=moneda_origen, to_currency=moneda_destino, amount=cantidad, api_key=API_KEY)

    response = requests.get(url)
    data = response.json()

    if 'result' in data:
        resultado = data['result']['amount']
        return jsonify({'resultado': resultado}), 200
    else:
        return jsonify({'error': 'Failed to convert currencies'})

