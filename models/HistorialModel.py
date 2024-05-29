from database.db import get_connection
from models.entities.Historial import Historial


class HistorialModel():

  @classmethod
  def getHistorial(self):
    try:
      cx = get_connection()
      historiales = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT ID_HistorialPrecio,ID_Producto ,Precio_Anterior  ,Precio_Nuevo,Fecha_Cambio FROM HistorialPrecio'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          historial = Historial(row[0], row[1], row[2], row[3], row[4])
          historiales.append(historial.to_JSON())
        cx.close()
        return historiales
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def add_Historial(self, historial):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute(
            "INSERT INTO historial VALUES(%s, %s, %s, %s, %s)",
            (historial.ID_HistorialPrecio , historial.ID_Producto ,
             historial.Precio_Anterior , historial.Precio_Nuevo , historial.Fecha_Cambio))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)