class Inventario():
    def __init__(self,
                ID_Inventario=None,
                 ID_Producto=None,
                 ID_Sucursal=None,
                 Cantidad_Disponible=None): 

       self.ID_Inventario = ID_Inventario, 
       self.ID_Producto = ID_Producto,
       self.ID_Sucursal = ID_Sucursal,
       self.Cantidad_Disponible = Cantidad_Disponible

    def to_JSON(self):
      return {
        'ID_Inventario': self.ID_Inventario,
        'ID_Producto': self.ID_Producto,
        'ID_Sucursal': self.ID_Sucursal,
        'Cantidad':self.Cantidad_Disponible
      }
      

