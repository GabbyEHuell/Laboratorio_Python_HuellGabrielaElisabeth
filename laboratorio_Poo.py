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
    def __init__(self, nombre, id, precio, stock , categoria, subcategoria, material, color): # Constructor de la clase.
        self.__nombre = nombre
        self.__id = id
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
        self.__subcategoria = subcategoria
        self.__material = material
        self.__color = color
    
    @property # Decorador para definir un método getter.
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def id(self):
        return self.__id

    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def categoria(self):
        return self.__categoria.capitalize()
    
    @property
    def subcategoria(self):
        return self.__subcategoria.capitalize()
    
    @property
    def material(self):
        return self.__material.capitalize()
    
    @property
    def color(self):
        return self.__color.capitalize()
    
    @nombre.setter # Decorador para definir un método setter.
    def nombre(self, nuevo_nombre): 
        self.__nombre = self.validar_nombre(nuevo_nombre)
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = self.validar_id(nuevo_id)
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)
    
    @stock.setter
    def stock(self, cantidad):
        self.__stock = self.validar_stock(cantidad)
    
    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = self.validar_categoria(nueva_categoria)
    
    @subcategoria.setter
    def subcategoria(self, nueva_subcategoria):
        self.__subcategoria = self.validar_subcategoria(nueva_subcategoria)
    
    @material.setter
    def material(self, nuevo_material):
        self.__material = self.validar_material(nuevo_material)
    
    @color.setter
    def color(self, nuevo_color):
        self.__color = self.validar_color(nuevo_color)

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el nombre no sea vacío y que no este repetido.
    def validar_nombre(self, nombre): 
        try:
            nombre_valido = nombre.capitalize()
            if not nombre_valido:
                raise ValueError("El nombre no puede estar vacío.") 
            return nombre_valido
        except ValueError:
            raise ValueError("El nombre no puede estar vacío.")  # Lanzar excepción
        
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el id sea valido
    def validar_id(self, id):
        try:
            id_valido = id
            if not id_valido:
                raise ValueError("El id no puede estar vacío.")
            return id_valido
        except ValueError:
             raise ValueError("El id no puede estar vacío.")
    
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
            raise ValueError("La cantidad no puede ser negativa.")
        
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que la categoría no sea vacía
    def validar_categoria(self, categoria):
        try:
            categoria_valida = categoria.capitalize()
            if not categoria_valida:
                raise ValueError("La categoría no puede estar vacía.")
            return categoria_valida
        except ValueError:
            raise ValueError("La categoría no puede estar vacía.")
    
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que la subcategoría sea Terminación o Borde
    def validar_subcategoria(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Terminación", "Borde"]:
                raise ValueError("El tipo de producto debe ser Terminación o Borde.")
            return tipo_valido
        except ValueError:
            raise ValueError("El tipo de producto debe ser Terminación o Borde.")
    
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el material no sea vacío
    def validar_material(self, material):
        try:
            material_valido = material.capitalize()
            if not material_valido:
                raise ValueError("El material no puede estar vacío.")
            return material_valido
        except ValueError:
            raise ValueError("El material no puede estar vacío.")
    
    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el color no sea vacío
    def validar_color(self, color):
        try:
            color_valido = color.capitalize()
            if not color_valido:
                raise ValueError("El color no puede estar vacío.")
            return color_valido
        except ValueError:
            raise ValueError("El color no puede estar vacío.")
    
    # Método para convertir la instancia en un diccionario y devolverlo como para poder serializarla a JSON.
    def to_dict(self): 
        return {
            "nombre": self.nombre, 
            "id": self.id, 
            "precio": self.precio, 
            "stock": self.stock, 
            "categoria": self.categoria, 
            "subcategoria": self.subcategoria, 
            "material": self.material, 
            "color": self.color}  
    # Métodos comunes para todas las instancias de Producto.
    
    def __str__(self):
        return f"Producto: {self.nombre}, Id: {self.id}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Subcategoría: {self.subcategoria}, Material: {self.material}, Color: {self.color}"

'''
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
'''
class ProductoPiscina(Producto):
    def __init__(self, nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta):
        super().__init__(nombre, id, precio, stock, categoria, subcategoria, material, color)
        self.__cantidad_unidad_venta = cantidad_unidad_venta
    
    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta.capitalize()

    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)
    

    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = cantidad.capitalize()
            if not cantidad_valida:
                raise ValueError("La cantidad de unidades del producto no puede estar vacía.")
            return cantidad_valida
        except ValueError:
            raise ValueError("La cantidad de unidades del producto no puede estar vacía.")
    
    def to_dict(self):
        data = super().to_dict()
        data["cantidad_unidad_venta"] = self.cantidad_unidad_venta
        return data
    
class ProductoTerminacion(ProductoPiscina):
    def __init__(self, nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_terminacion):
        super().__init__(nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta)
        self.__tipo_terminacion = tipo_terminacion
    
    @property
    def tipo_terminacion(self):
        return self.__tipo_terminacion.capitalize()
    
    @tipo_terminacion.setter
    def tipo_terminacion(self, nuevo_tipo):
        self.__tipo_terminacion = self.validar_tipo(nuevo_tipo)
    
    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Pintura", "Revestimiento", "Impermeabilizante"]:
                raise ValueError("El tipo de producto debe ser Pintura, Revestimiento o Impermeabilizante.")
            return tipo_valido
        except ValueError:
            raise ValueError("El tipo de producto debe ser Pintura, Revestimiento o Impermeabilizante.")
    
    # Métodos específicos para productos de terminación.
    def to_dict(self):
        data = super().to_dict()
        data["tipo_terminacion"] = self.tipo_terminacion
        return data
        
    def __str__(self):
        return f"Producto: {self.nombre}, Id: {self.id}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Tipo de terminación: {self.tipo_terminacion}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}"

class ProductoBorde(ProductoPiscina):
    def __init__(self, nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_borde, largo, ancho, espesor):
        super().__init__(nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta)
        self.__tipo_borde = tipo_borde
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor
    
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

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ["Borde ballena", "Borde recto", "Borde l", "Esquina ballena", "Esquina recta", "Esquina l"]:
                raise ValueError("El tipo de borde debe ser Borde ballena, Borde recto, Borde l, Esquina ballena, Esquina recta o Esquina l.")
            return tipo_valido
        except ValueError:
            raise ValueError("El tipo de borde debe ser Borde ballena, Borde recto, Borde l, Esquina ballena, Esquina recta o Esquina l.")
        
    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError("La medida no puede ser negativa.")
            return medida_valida
        except ValueError:
            raise ValueError("La medida no puede ser negativa.")
        
    # Métodos específicos para productos de borde.
    def to_dict(self):
        data = super().to_dict()
        data["tipo_borde"] = self.tipo_borde
        data["largo"] = self.largo
        data["ancho"] = self.ancho
        data["espesor"] = self.espesor
        return data
    
    def __str__(self):
        return f"Producto: {self.nombre}, Id: {self.id}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Tipo de borde: {self.tipo_borde}, Largo: {self.largo} cm, Ancho: {self.ancho} cm, Espesor: {self.espesor} cm, Cantidad de unidad x venta: {self.cantidad_unidad_venta}"

class ProductoRevestimiento(Producto):
    def __init__(self, nombre, id, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_superficie, ubicacion,
                 largo, ancho, espesor):
        super().__init__(nombre, id, precio, stock, categoria, subcategoria, material, color)
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad_unidad_venta)
        self.__tipo_superficie = tipo_superficie  # Piso, pared o ambas
        self.__ubicacion = ubicacion # Interior, exterior o ambas
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor
    
    
    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta
    
    @property
    def tipo_superficie(self):
        return self.__tipo_superficie.capitalize()
    
    @property
    def ubicacion(self):
        return self.__ubicacion.capitalize()
        
    @property
    def largo(self):
        return self.__largo
    
    @property
    def ancho(self):
        return self.__ancho
    
    @property
    def espesor(self):
        return self.__espesor
        
    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)
    
    @tipo_superficie.setter
    def tipo_superficie(self, nuevo_tipo):
        self.__tipo_superficie = self.validar_tipo(nuevo_tipo)
    
    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = self.validar_ubicacion(nueva_ubicacion)


    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = self.validar_medida(nuevo_largo)
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = self.validar_medida(nuevo_ancho)
    
    @espesor.setter
    def espesor(self, nuevo_espesor):
        self.__espesor = self.validar_medida(nuevo_espesor)
    
    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = int(cantidad)  # Convertimos la cantidad a un entero
            if cantidad_valida <= 0:
                raise ValueError("La cantidad de unidades del producto debe ser mayor que cero.")
            return cantidad_valida
        except ValueError:
            print("La cantidad de unidades del producto debe ser un número entero mayor que cero.")
            return None  # Devolvemos None en caso de error para manejarlo más adelante
   
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
    
    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError("La medida no puede ser negativa.")
            return medida_valida
        except ValueError:
            raise ValueError("La medida debe ser un número válido.")
    
    # Métodos específicos para ProductoRevestimiento.
    def to_dict(self):
        data = super().to_dict()
        data["cantidad_unidad_venta"] = self.cantidad_unidad_venta
        data["tipo_superficie"] = self.tipo_superficie
        data["ubicacion"] = self.ubicacion
        data["largo"] = self.largo
        data["ancho"] = self.ancho
        data["espesor"] = self.espesor
        return data

    def __str__(self):
        return f"Producto: {self.nombre}, Id: {self.id}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Subcategoría: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Tipo de superficie: {self.tipo_superficie}, Ubicación: {self.ubicacion}, Largo: {self.largo} cm, Ancho: {self.ancho} cm, Espesor: {self.espesor} cm, Cantidad de unidad x venta: {self.cantidad_unidad_venta}"
class ProductoAdicionales(Producto):
    def __init__(self, nombre, id, precio, stock, categoria, subcategoria, material, color, uso_funcion):
        super().__init__(nombre, id, precio, stock , categoria, subcategoria, material, color)
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
        return f"Producto: {self.nombre}, Id: {self.id}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Uso o función: {self.uso_funcion}, Material: {self.material}, Color: {self.color}"
    
    
''' 
Implementar operaciones CRUD para gestionar productos del inventario.
'''
class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo
    
    # Método para traer los datos del archivo JSON y leer
    def leer_datos(self):
        try:
            with open(self.archivo, "r") as file:
                content = file.read()
                if content:
                    datos = json.loads(content)
                else:
                    datos = {}  # Si el archivo está vacío, se retorna un diccionario vacío.
        except FileNotFoundError:
            datos = {} # Si no existe el archivo, se retorna un diccionario vacío.
        except json.JSONDecodeError:
            datos = {}  # Si hay un error al decodificar JSON, también se retorna un diccionario vacío.
        except Exception as error:  # Si ocurre un error, se imprime el mensaje de error.
            raise Exception(f"Encontramos un error al leer el archivo: {error}")
        else:
            return datos
    
    # Método para escribir "guardar" los datos en el archivo JSON
    def escribir_datos(self, datos):
        try:
            with open(self.archivo, "w") as file:
                json.dump(datos, file, indent=4)
        except IOError as e:
            raise IOError(f"Error al intentar guardar los datos en el archivo {self.archivo}: {e}")
        except Exception as e:
            raise Exception(f"Error inesperado al escribir en el archivo: {e}")
    
    # Método para "crear" un producto y agregarlo al inventario.
    def crear_producto(self, producto):
        try:
            datos = self.leer_datos()
            id = producto.id
            # Aplicar validacion para verificar que ya no exista un producto con el mismo nombre. 
            if not str(id) in datos.keys():
                datos[id] = producto.to_dict()
                self.escribir_datos(datos)
                print(f"Producto {producto.nombre} agregado correctamente.")
            else:
                print(f"El producto con codigo {id} ya existe en el inventario. Intente con un ID diferente.")
                return  # Agrega esta línea para detener la ejecución si el ID ya existe
        except Exception as error:
            print(f"Error al agregar el producto: {error}")

    # Método para buscar un producto por su nombre que seria leer un productos.
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.nombre == nombre:
                return producto
        return None
    
    def actualizar_producto(self, nombre, id, nuevo_precio, nuevo_stock):
        producto = self.buscar_producto(id)
        if producto:
            producto.nombre = nombre
            producto.precio = nuevo_precio
            producto.stock = nuevo_stock
        else:
            print("El producto no existe.")
    
    def eliminar_producto(self, id):
        producto = self.buscar_producto(id)
        if producto:
            self.__productos.remove(producto)
        else:
            print("El producto no existe.")
    
    def listar_productos(self):
        for producto in self.__productos:
            print(producto)
    
    # Método para guardar el inventario en un archivo JSON.
    def guardar_inventario(self, archivo):
        with open(archivo, "w") as file:
            json.dump([producto.to_dict() for producto in self.__productos], file, indent=4)
    
    def cargar_inventario(self, archivo):
        with open(archivo, "r") as file:
            datos = json.load(file)
            for producto in datos:
                if producto["tipo"] == "ProductoRevestimiento":
                    producto = ProductoRevestimiento(producto["nombre"], producto["precio"], producto["stock"],
                                                     producto["categoria"], producto["tipo_superficie"],
                                                     producto["ubicacion"], producto["material"], producto["color"],
                                                     producto["largo"], producto["ancho"], producto["espesor"])
                elif producto["tipo"] == "ProductoTerminacion":
                    producto = ProductoTerminacion(producto["nombre"], producto["precio"], producto["stock"],
                                                   producto["categoria"], producto["tipo_terminacion"],
                                                   producto["material"], producto["color"],
                                                   producto["cantidad_unidad_venta"])
                elif producto["tipo"] == "ProductoBorde":
                    producto = ProductoBorde(producto["nombre"], producto["precio"], producto["stock"],
                                             producto["categoria"], producto["tipo_borde"], producto["material"],
                                             producto["color"], producto["largo"], producto["ancho"],
                                             producto["espesor"], producto["cantidad_unidad_venta"])
                elif producto["tipo"] == "ProductoAdicionales":
                    producto = ProductoAdicionales(producto["nombre"], producto["precio"], producto["stock"],
                                                   producto["categoria"], producto["uso_funcion"], producto["material"],
                                                   producto["color"])
                self.__productos.append(producto)
    

