
from flask import request, jsonify, Blueprint
import requests

main = Blueprint("Moneda", __name__)


API_KEY = '52621|PFxrMwNyeYeyo1t9Ug0w'
CAMBIO_TODAY_API_URL = 'https://api.cambio.today/v1/quotes/{from_currency}/{to_currency}/json?quantity={amount}&key={api_key}'

@main.route('/convertir_monedas', methods=['POST'])
def convertir_monedas():
    data = request.json

    if data is None:
        return jsonify({'error': 'No data provided'})

    cantidad = data.get('cantidad')
    if cantidad is None:
        return jsonify({'error': 'Missing cantidad in request'})

    moneda_origen = data.get('moneda_origen')
    if moneda_origen is None:
        return jsonify({'error': 'Missing moneda_origen in request'})

    moneda_destino = data.get('moneda_destino')
    if moneda_destino is None:
        return jsonify({'error': 'Missing moneda_destino in request'})

    url = CAMBIO_TODAY_API_URL.format(from_currency=moneda_origen, to_currency=moneda_destino, amount=cantidad, api_key=API_KEY)

    response = requests.get(url)
    data = response.json()

    if 'result' in data:
        resultado = data['result']['amount']
        return jsonify({'resultado': resultado})
    else:
        return jsonify({'error': 'Failed to convert currencies'})

