class Producto():

    def __init__(self,
                 ID_Producto=None,
                 Nombre=None,
                 Descripcion=None,
                 Precio_Base=None,
                 ID_Categoria=None,
                 Estado=None,
                 Fecha_Inicio_Estado=None,
                 Fecha_Fin_Estado=None):
        self.ID_Producto = ID_Producto
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Precio_Base = Precio_Base
        self.ID_Categoria = ID_Categoria
        self.Estado = Estado
        self.Fecha_Inicio_Estado = Fecha_Inicio_Estado
        self.Fecha_Fin_Estado = Fecha_Fin_Estado

    def to_JSON(self):
        return {
            'ID_Producto': self.ID_Producto,
            'Nombre': self.Nombre,
            'Descripcion': self.Descripcion,
            'Precio_Base': self.Precio_Base,
            'ID_Categoria': self.ID_Categoria,
            'Estado': self.Estado,
            'Fecha_Inicio_Estado': self.Fecha_Inicio_Estado,
            'Fecha_Fin_Estado': self.Fecha_Fin_Estado
        }


class Productocat():
    def __init__(self,
                 Nombre_Categoria=None,
                 Nombre_Producto=None,
                 Precio=None):
        self.Nombre_Categoria = Nombre_Categoria
        self.Nombre_Producto = Nombre_Producto
        self.Precio = Precio

    def to_JSON(self):
        return {
            'Nombre_Categoria': self.Nombre_Categoria,
            'Nombre_Producto': self.Nombre_Producto,
            'Precio': self.Precio
        }
                    