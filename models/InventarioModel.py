from database.db import get_connection
from models.entities.Inventario import Inventario

class InventarioModel():
  @classmethod
  def getInventario(self):
    try:
      cx = get_connection()
      inventarios = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT ID_Inventario, ID_Producto, ID_Sucursal, Cantidad_Disponible FROM inventario'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          inventario = Inventario(row[0], row[1], row[2], row[3])
          inventarios.append(inventario.to_JSON())
        cx.close()
        return inventarios
    except Exception as ex:
      raise Exception(ex)
