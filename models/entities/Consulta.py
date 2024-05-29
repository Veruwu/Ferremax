class Consulta():
    def __init__(self,
                 ID=None,
                 Rut_Cliente=None,
                 Rut_Vendedor=None,
                 Mensaje=None,
                 Fecha=None
):
      self.ID = ID
      self.Rut_Cliente = Rut_Cliente
      self.Rut_Vendedor = Rut_Vendedor
      self.Mensaje = Mensaje
      self.Fecha = Fecha

    def to_JSON(self):
        return {
            "ID": self.ID,
            "Rut_Cliente": self.Rut_Cliente,
            "Rut_Vendedor": self.Rut_Vendedor,
            "Mensaje": self.Mensaje,
            "Fecha": self.Fecha
        }