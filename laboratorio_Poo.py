'''
Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.

'''
'''
Crear una clase base Producto con atributos como ProductoId, Nombre, CategoriaId, Stock, Habilitado, Precio, Color, Medida, Material
'''
import json

class Producto:
    def __init__(self, nombre, precio, stock , categoria): # Constructor de la clase.
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
    
    @property # Decorador para definir un método getter.
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def categoria(self):
        return self.__categoria.capitalize()
    
    @nombre.setter # Decorador para definir un método setter.
    def nombre(self, nuevo_nombre): 
        self.__nombre = self.validar_nombre(nuevo_nombre)
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)
    
    @stock.setter
    def stock(self, cantidad):
        self.__stock = self.validar_stock(cantidad)
    
    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = self.validar_categoria(nueva_categoria)

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el nombre no sea vacío
    def validar_nombre(self, nombre):
        try:
            nombre_valido = nombre.capitalize()
            if not nombre_valido:
                raise ValueError("El nombre no puede estar vacío.")
            return nombre_valido 
        except ValueError:
            print("El nombre no puede estar vacío.")
    
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el precio sea mayor o igual a 0
    def validar_precio(self, precio):
        try:
            precio_valido = float(precio)
            if precio_valido < 0:
                raise ValueError("El precio no puede ser negativo.")
            return precio_valido
        except ValueError:
            raise ValueError("El precio no puede ser negativo.")

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el stock sea mayor o igual a 0
    def validar_stock(self, cantidad):
        try:
            cantidad_valida = int(cantidad)
            if cantidad_valida < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            return cantidad_valida
        except ValueError:
            print("La cantidad no puede ser negativa.")
        
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que la categoría no sea vacía
    def validar_categoria(self, categoria):
        try:
            categoria_valida = categoria.capitalize()
            if not categoria_valida:
                raise ValueError("La categoría no puede estar vacía.")
            return categoria_valida
        except ValueError:
            print("La categoría no puede estar vacía.")
    
    # Método para convertir la instancia en un diccionario y devolverlo como para poder serializarla a JSON.
    def to_dict(self): 
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria
        }
    # Métodos comunes para todas las instancias de Producto.
    

'''
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
'''
class ProductoPiscina(Producto):
    def __init__(self, nombre, precio, stock, categoria, tipo_terminacion_borde, material, color):
        super().__init__(nombre, precio, stock, categoria)
        self.tipo_terminacion_borde = tipo_terminacion_borde # Terminación o borde
        self.material = material # Cemento, atermico, Cerámica, texturado, pintura, madera etc.
        self.color = color

    # Métodos específicos para ProductoPiscina.

class ProductoTerminacion(ProductoPiscina):
    def __init__(self, nombre, precio, stock, categoria, tipo_terminacion, material, color,
                 cantidad_unidad_venta):
        super().__init__(nombre, precio, stock, categoria, tipo_terminacion_borde="Terminación",
                         material=material, color=color)
        self.tipo_terminacion = tipo_terminacion
        self.cantidad_unidad_venta = cantidad_unidad_venta
    # Métodos específicos para productos de terminación o revestimiento.

    def to_dict(self):
        data = super().to_dict()
        data["tipo_Terminacion"] = self.tipo_terminacion
        data["cantidad_unidad_venta"] = self.cantidad_unidad_venta
        return data
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.tipo_terminacion}, Material: {self.material}, Color: {self.color}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}"
    

class ProductoBorde(ProductoPiscina):
    def __init__(self, nombre, precio, stock, categoria, tipo_borde, material, color,
                 largo, ancho, espesor, cantidad_unidad_venta):
        super().__init__(nombre, precio, stock, categoria, tipo_terminacion_borde="Borde",
                         material=material, color=color)
        self.tipo_borde = tipo_borde
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor
        self.cantidad_unidad_venta = cantidad_unidad_venta
    # Métodos específicos para productos de bordes o coronaciones.

    def to_dict(self):
        data = super().to_dict()
        data["tipo_Borde"] = self.tipo_borde
        data["largo"] = self.largo
        data["ancho"] = self.ancho
        data["espesor"] = self.espesor
        data["cantidad_unidad_venta"] = self.cantidad_unidad_venta
        return data
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.tipo_borde}, Material: {self.material}, Color: {self.color}, Largo: {self.largo}, Ancho: {self.ancho}, Espesor: {self.espesor}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}"

class ProductoRevestimiento(Producto):
    def __init__(self, nombre, precio, stock, categoria, tipo_superficie, ubicacion, material, color,
                 largo, ancho, espesor):
        super().__init__(nombre, precio, stock, categoria)
        self.tipo_superficie = tipo_superficie  # Piso, pared o ambas
        self.ubicacion = ubicacion  # Interior, exterior o ambas
        self.material = material # Cemento, atermico, Cerámica, texturado, etc.
        self.color = color
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor
        # Métodos específicos para ProductoRevestimiento.
    def to_dict(self):
        data = super().to_dict()
        data["tipo_superficie"] = self.tipo_superficie
        data["ubicacion"] = self.ubicacion
        data["material"] = self.material
        data["color"] = self.color
        data["largo"] = self.largo
        data["ancho"] = self.ancho
        data["espesor"] = self.espesor
        return data    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de superficie: {self.tipo_superficie}, Ubicación: {self.ubicacion}, Material: {self.material}, Color: {self.color}, Largo: {self.largo} cm, Ancho: {self.ancho} cm, Espesor: {self.espesor} cm"

class ProductoAdicionales(Producto):
    def __init__(self, nombre, precio, stock, categoria, uso_funcion):
        super().__init__(nombre, precio, stock , categoria)
        self.uso_funcion = uso_funcion
    # Métodos específicos para ProductoAdicionales.

    def to_dict(self):
        data = super().to_dict()
        data["uso_funcion"] = self.uso_funcion
        return data
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Uso o función: {self.uso_funcion}"
