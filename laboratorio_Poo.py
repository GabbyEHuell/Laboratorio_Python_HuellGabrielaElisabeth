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
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}"
    

'''
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
'''
class ProductoPiscina(Producto):
    def __init__(self, nombre, precio, stock, categoria, tipo_terminacion_borde, material, color):
        super().__init__(nombre, precio, stock, categoria)
        self.__tipo_terminacion_borde = tipo_terminacion_borde # Terminación o borde
        self.__material = material # Cemento, atermico, Cerámica, texturado, pintura, madera etc.
        self.__color = color
    
    @property
    def tipo_terminacion_borde(self):
        return self.__tipo_terminacion_borde.capitalize()
    
    @property
    def material(self):
        return self.__material.capitalize()
    
    @property
    def color(self):
        return self.__color.capitalize()
    
    @tipo_terminacion_borde.setter
    def tipo_terminacion_borde(self, nuevo_tipo):
        self.__tipo_terminacion_borde = self.validar_tipo(nuevo_tipo)
    
    @material.setter
    def material(self, nuevo_material):
        self.__material = self.validar_material(nuevo_material)
    
    @color.setter
    def color(self, nuevo_color):
        self.__color = self.validar_color(nuevo_color)
    # Métodos específicos para ProductoPiscina.

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Terminación", "Borde"]:
                raise ValueError("El tipo de producto debe ser Terminación o Borde.")
            return tipo_valido
        except ValueError:
            print("El tipo de producto debe ser Terminación o Borde.")
    
    def validar_material(self, material):
        try:
            material_valido = material.capitalize()
            if not material_valido:
                raise ValueError("El material no puede estar vacío.")
            return material_valido
        except ValueError:
            print("El material no puede estar vacío.")
    
    def validar_color(self, color):
        try:
            color_valido = color.capitalize()
            if not color_valido:
                raise ValueError("El color no puede estar vacío.")
            return color_valido
        except ValueError:
            print("El color no puede estar vacío.")


class ProductoTerminacion(ProductoPiscina):
    def __init__(self, nombre, precio, stock, categoria, tipo_terminacion, material, color,
                 cantidad_unidad_venta):
        super().__init__(nombre, precio, stock, categoria, tipo_terminacion_borde="Terminación",
                         material=material, color=color)
        self.__tipo_terminacion = tipo_terminacion
        self.__cantidad_unidad_venta = cantidad_unidad_venta
    
    @property
    def tipo_terminacion(self):
        return self.__tipo_terminacion.capitalize()
    
    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta
    
    @tipo_terminacion.setter
    def tipo_terminacion(self, nuevo_tipo):
        self.__tipo_terminacion = self.validar_tipo(nuevo_tipo)
    
    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)
    
    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = cantidad.capitalize()
            if not cantidad_valida:
                raise ValueError("La cantidad no puede estar vacía.")
            return cantidad_valida
        except ValueError:
            print("La cantidad no puede estar vacía.")
    
    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Terminación"]:
                raise ValueError("El tipo de producto debe ser Terminación.")
            return tipo_valido
        except ValueError:
            print("El tipo de producto debe ser Terminación.")

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
        self.__tipo_borde = tipo_borde
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor
        self.__cantidad_unidad_venta = cantidad_unidad_venta
    
    @property
    def tipo_borde(self):
        return self.__tipo_borde.capitalize()
    
    @property
    def largo(self):
        return self.__largo
    
    @property
    def ancho(self):
        return self.__ancho
    
    @property
    def espesor(self):
        return self.__espesor
    
    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta
    
    @tipo_borde.setter
    def tipo_borde(self, nuevo_tipo):
        self.__tipo_borde = self.validar_tipo(nuevo_tipo)
    
    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = self.validar_medida(nuevo_largo)
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = self.validar_medida(nuevo_ancho)
    
    @espesor.setter
    def espesor(self, nuevo_espesor):
        self.__espesor = self.validar_medida(nuevo_espesor)
    
    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)
    
    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Borde Ballena", "Borde Recto", "Borde L"]:
                raise ValueError("El tipo de producto debe ser Borde Ballena, Borde Recto o Borde L.")
            return tipo_valido
        except ValueError:
            print("El tipo de producto debe ser Borde Ballena, Borde Recto o Borde L.")
    
    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError("La medida no puede ser negativa.")
            return medida_valida
        except ValueError:
            print("La medida no puede ser negativa.")
    
    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = cantidad.capitalize()
            if not cantidad_valida:
                raise ValueError("La cantidad no puede estar vacía.")
            return cantidad_valida
        except ValueError:
            print("La cantidad no puede estar vacía.")

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
        self.__tipo_superficie = tipo_superficie  # Piso, pared o ambas
        self.__ubicacion = ubicacion  # Interior, exterior o ambas
        self.__material = material # Cemento, atermico, Cerámica, texturado, etc.
        self.__color = color
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor

    @property
    def tipo_superficie(self):
        return self.__tipo_superficie.capitalize()
    
    @property
    def ubicacion(self):
        return self.__ubicacion.capitalize()
    
    @property
    def material(self):
        return self.__material.capitalize()
    
    @property
    def color(self):
        return self.__color.capitalize()
    
    @property
    def largo(self):
        return self.__largo
    
    @property
    def ancho(self):
        return self.__ancho
    
    @property
    def espesor(self):
        return self.__espesor
    
    @tipo_superficie.setter
    def tipo_superficie(self, nuevo_tipo):
        self.__tipo_superficie = self.validar_tipo(nuevo_tipo)
    
    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = self.validar_ubicacion(nueva_ubicacion)
    
    @material.setter
    def material(self, nuevo_material):
        self.__material = self.validar_material(nuevo_material)
    
    @color.setter
    def color(self, nuevo_color):
        self.__color = self.validar_color(nuevo_color)
    
    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = self.validar_medida(nuevo_largo)
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = self.validar_medida(nuevo_ancho)
    
    @espesor.setter
    def espesor(self, nuevo_espesor):
        self.__espesor = self.validar_medida(nuevo_espesor)

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Piso", "Pared", "Ambas"]:
                raise ValueError("El tipo de superficie debe ser Piso, Pared o Ambas.")
            return tipo_valido
        except ValueError:
            print("El tipo de superficie debe ser Piso, Pared o Ambas.")
    
    def validar_ubicacion(self, ubicacion):
        try:
            ubicacion_valida = ubicacion.capitalize()
            if ubicacion_valida not in ["Interior", "Exterior", "Ambas"]:
                raise ValueError("La ubicación debe ser Interior, Exterior o Ambas.")
            return ubicacion_valida
        except ValueError:
            print("La ubicación debe ser Interior, Exterior o Ambas.")  
    
    def validar_material(self, material):
        try:
            material_valido = material.capitalize()
            if not material_valido:
                raise ValueError("El material no puede estar vacío.")
            return material_valido
        except ValueError:
            print("El material no puede estar vacío.")
    
    def validar_color(self, color):
        try:
            color_valido = color.capitalize()
            if not color_valido:
                raise ValueError("El color no puede estar vacío.")
            return color_valido
        except ValueError:
            print("El color no puede estar vacío.")
    
    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError("La medida no puede ser negativa.")
            return medida_valida
        except ValueError:
            print("La medida no puede ser negativa.")
    
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
        self.__uso_funcion = uso_funcion
    
    @property
    def uso_funcion(self):
        return self.__uso_funcion.capitalize()
    
    @uso_funcion.setter
    def uso_funcion(self, nuevo_uso):
        self.__uso_funcion = self.validar_uso(nuevo_uso)
    
    def validar_uso(self, uso):
        try:
            uso_valido = uso.capitalize()
            if not uso_valido:
                raise ValueError("El uso o función no puede estar vacío.")
            return uso_valido
        except ValueError:
            print("El uso o función no puede estar vacío.")
    
    # Métodos específicos para ProductoAdicionales.

    def to_dict(self):
        data = super().to_dict()
        data["uso_funcion"] = self.uso_funcion
        return data
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Uso o función: {self.uso_funcion}"
