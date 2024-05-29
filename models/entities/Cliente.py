class Cliente():

    def __init__(self,
                 Rut_Cliente=None,
                 Nombre=None,
                 Correo=None,
                 Contrasena=None,
):
      self.Rut_Cliente = Rut_Cliente
      self.Nombre = Nombre
      self.Correo = Correo
      self.Contrasena = Contrasena
    
    def to_JSON(self):
      return {
          'Correo': self.Correo,
          'Nombre': self.Nombre,
          'Rut_Cliente': self.Rut_Cliente
      }