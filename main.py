from flask import Flask
from models.entities import Inventario
from routes import Cliente, Historial, Producto, Vendedor, Mensaje, Moneda, Inventario

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

# Blueprint
app.register_blueprint(Producto.main, url_prefix='/api/productos')
app.register_blueprint(Historial.main, url_prefix='/api/historial')
app.register_blueprint(Cliente.main, url_prefix='/api/clientes')
app.register_blueprint(Vendedor.main, url_prefix='/api/vendedores')
app.register_blueprint(Mensaje.main, url_prefix='/api/mensajes')
app.register_blueprint(Moneda.main, url_prefix='/api/moneda')
app.register_blueprint(Inventario.main, url_prefix='/api/inventario')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
