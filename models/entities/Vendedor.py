class Vendedor():

    def __init__(self,
                 Rut_Vendedor=None,
                 Nombre=None,
                 Correo=None,
                 Contrasena=None,
):
      self.Rut_Vendedor = Rut_Vendedor
      self.Nombre = Nombre
      self.Correo = Correo
      self.Contrasena = Contrasena

    def to_JSON(self):
      return {
          'Correo': self.Correo,
          'Nombre': self.Nombre,
          'Rut_Vendedor': self.Rut_Vendedor
      }