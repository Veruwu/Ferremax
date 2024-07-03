from database.db import get_connection
from models.entities.Vendedor import Vendedor
from itertools import cycle
from flask import request
import bcrypt


class VendedorModel():
  @classmethod
  def getVendedor(self):
    try:
      cx = get_connection()
      vendedores = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT Rut_Vendedor,Nombre,Correo,Contrasena FROM vendedor'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          vendedor = Vendedor(row[0], row[1], row[2], row[3])
          vendedores.append(vendedor.to_JSON())
        cx.close()
        return vendedores
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def digito_verificador(self, Rut_Vendedor):
    try:
      rut = Rut_Vendedor.replace('.', '').replace('-', '')
      aux = rut[:-1]
      dv = rut[-1:]

      revertido = map(int, reversed(str(aux)))
      factors = cycle(range(2,8))
      s = sum(d * f for d, f in zip(revertido,factors))
      res = (-s)%11

      if str(res) == dv:
        return True
      elif dv=="K" and res==10:
        return True
      else:
        return False
    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def add_Vendedor(self, vendedor):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        enc_pwd = bcrypt.hashpw(vendedor.Contrasena.encode("utf-8"),
                                bcrypt.gensalt(10))
        rutv = self.digito_verificador(vendedor.Rut_Vendedor)
        cursor.execute(
            "INSERT INTO vendedor VALUES(%s, %s, %s, %s)",
            (vendedor.Rut_Vendedor, vendedor.Nombre, vendedor.Correo, (enc_pwd.decode())))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def delete_Vendedor(self, Rut_Vendedor):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute(
            "DELETE FROM vendedor WHERE Rut_Vendedor='{0}'::text".format(Rut_Vendedor))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def login(self, vendedor):
    try:
      cx = get_connection()
      data = request.get_json()
      correo = data['correo']
      contrasena = data['contrasena'].encode('utf-8')

      with cx.cursor() as cursor:

        query = "SELECT correo, contrasena FROM vendedor WHERE correo = 'PARAMETRO'"
        consulta_parametro = query.replace("PARAMETRO", str(vendedor.Correo))
        #print("query: "+consulta_parametro)
        cursor.execute(consulta_parametro)

        resultset = cursor.fetchone()

        if resultset and bcrypt.checkpw(contrasena,
                                        resultset[1].encode('utf-8')):
          return True
        else:
          return False

    except Exception as ex:
      raise Exception(ex)