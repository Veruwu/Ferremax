from database.db import get_connection
from models.entities.Producto import Producto, Productocat


class ProductoModel():

  @classmethod
  def getProducto(self):
    try:
      cx = get_connection()
      productos = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT ID_Producto,Nombre,Descripcion,Precio_Base,ID_Categoria,Estado,Fecha_Inicio_Estado,Fecha_Fin_Estado FROM producto'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5],
                              row[6], row[7])
          productos.append(producto.to_JSON())
        cx.close()
        return productos
    except Exception as ex:
      raise Exception(ex)
      
  @classmethod
  def getProductoCat(self, ID_Categoria):
    try:
      cx = get_connection()
      productos = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT c.Nombre_Categoria,p.Nombre AS Nombre_Producto,p.Precio_Base FROM producto p JOIN categoria c ON p.ID_Categoria = c.ID_Categoria where c.ID_Categoria = %s',(ID_Categoria)
        )
        resultset = cursor.fetchall()
        for row in resultset:
          producto = Productocat(row[0], row[1], row[2])
          productos.append(producto.to_JSON())
        cx.close()
        return productos
    except Exception as ex:
      raise Exception(ex)

  

  @classmethod
  def add_Producto(self, producto):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute(
            "INSERT INTO producto VALUES(nextval('producto_sequence'), %s, %s, %s, %s, %s)",
            (producto.Nombre,
             producto.Descripcion, producto.Precio_Base, producto.ID_Categoria, producto.Fecha_Inicio_Estado))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def update_Producto(self, producto, ID_Producto):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute(
            "UPDATE producto SET Nombre = %s, Descripcion = %s, Precio_Base = %s, ID_Categoria = %s WHERE ID_Producto = %s",
            (producto.Nombre, producto.Descripcion, producto.Precio_Base,
             producto.ID_Categoria,(ID_Producto)))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
        
    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def delete_Producto(self, ID_Producto):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute(
            "DELETE FROM producto WHERE ID_Producto = {0}".format(ID_Producto))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows

    except Exception as ex:
      raise Exception(ex)
    