import psycopg2
from psycopg2 import DatabaseError

import os

def get_connection():
  try:
    # Obtiene el string de conexión almacenada en la variable de entorno
    cx_string = os.environ['CONNECTION_URL']
    cx = psycopg2.connect(dsn = cx_string)
    return cx
  except DatabaseError as ex:
    raise ex