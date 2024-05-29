from database.db import get_connection
from models.entities.Cliente import Cliente
from itertools import cycle
from flask import request
import bcrypt


class ClienteModel():
  @classmethod
  def getCliente(self):
    try:
      cx = get_connection()
      clientes = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT Rut_Cliente,Nombre,Correo,Contrasena FROM cliente'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          cliente = Cliente(row[0], row[1], row[2], row[3])
          clientes.append(cliente.to_JSON())
        cx.close()
        return clientes
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def digito_verificador(self, Rut_Cliente):
    try:
      rut = Rut_Cliente.replace('.', '').replace('-', '')
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
  def add_Cliente(self, cliente):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        enc_pwd = bcrypt.hashpw(cliente.Contrasena.encode("utf-8"),
                                bcrypt.gensalt(10))
        rutv = self.digito_verificador(cliente.Rut_Cliente)
        cursor.execute(
            "INSERT INTO cliente VALUES(%s, %s, %s, %s)",
            (cliente.Rut_Cliente, cliente.Nombre, cliente.Correo, (enc_pwd.decode())))
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)
      

  @classmethod
  def login(self, cliente):
    try:
      cx = get_connection()
      data = request.get_json()
      correo = data['correo']
      contrasena = data['contrasena'].encode('utf-8')

      with cx.cursor() as cursor:

        query = "SELECT correo, contrasena FROM cliente WHERE correo = 'PARAMETRO'"
        consulta_parametro = query.replace("PARAMETRO", str(cliente.Correo))
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