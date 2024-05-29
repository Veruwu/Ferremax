class Historial():

    def __init__(self,
                 ID_HistorialPrecio=None,
                 ID_Producto =None,
                 Precio_Anterior =None,
                 Precio_Nuevo=None,
                 Fecha_Cambio =None):
        self.ID_HistorialPrecio  = ID_HistorialPrecio 
        self.ID_Producto  = ID_Producto 
        self.Precio_Anterior  = Precio_Anterior 
        self.Precio_Nuevo  = Precio_Nuevo 
        self.Fecha_Cambio  = Fecha_Cambio 

    def to_JSON(self):
        return {
            'ID_HistorialPrecio': self.ID_HistorialPrecio,
            'ID_Producto': self.ID_Producto,
            'Precio_Anterior': self.Precio_Anterior,
            'Precio_Nuevo': self.Precio_Nuevo,
            'Fecha_Cambio': self.Fecha_Cambio,
        }

