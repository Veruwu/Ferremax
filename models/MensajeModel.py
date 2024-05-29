from database.db import get_connection
from models.entities.Consulta import Consulta

class MensajesModel():
    @classmethod
    def get_Mensaje(self, ID_Cliente):
        try:
            cx = get_connection()
            mensajes = []
            with cx.cursor() as cursor:
                cursor.execute(
                    'SELECT ID_Mensaje, ID_Cliente, ID_Vendedor, Fecha_Mensaje, Estado, Mensaje FROM mensajes WHERE ID_Cliente = %s',
                    (ID_Cliente))
                resultset = cursor.fetchall()
                for row in resultset:
                    mensaje = Consulta(row[0], row[1], row[2], row[3], row[4],
                                       row[5])
                    mensajes.append(mensaje.to_JSON())
                cx.close()
                return mensajes
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_Mensaje(self, mensaje, Rut_Cliente):
        try:
            cx = get_connection()
            with cx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO consultas VALUES(DEFAULT,%s, '200194349', %s,CURRENT_TIMESTAMP)",
                    ((Rut_Cliente), mensaje.Mensaje))
                affected_rows = cursor.rowcount
                cx.commit()
            cx.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)