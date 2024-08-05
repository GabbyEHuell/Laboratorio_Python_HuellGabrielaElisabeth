import os
import platform
import json

from laboratorio_Poo import Inventario, ProductoTerminacion, ProductoBorde, ProductoRevestimiento, ProductoAdicionales

filename = 'productos_db.json'

if not os.path.exists(filename):
    # Crea un archivo JSON vacío si no existe
    with open(filename, 'w') as fp:
        pass
else:
    print(f'El archivo {filename} ya existe.')

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs


def mostrar_menu():
    print("========== Menú de Gestión de de Productos ==========")
    print('1. Agregar Productos de piscina')
    print('2. Agregar Productos de revestiminetos')
    print('3. Agregar Productos adicionales')
    print('4. Buscar Productos por nombre')
    print('5. Actualizar Productos')
    print('6. Eliminarar Productos por nombre')
    print('7. Mostrar Todos los Productos')
    print('8. Salir')
    print('======================================================')

def obtener_categoria():
    while True:
        try:
            opcion = int(input("Seleccione una categoría:\n1. Piscina\n2. Revestimiento\n3. Adicionales\n"))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return "Piscina"
                elif opcion == 2:
                    return "Revestimiento"
                elif opcion == 3:
                    return "Adicionales"
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido (1, 2 o 3).")

def obtener_subcategoria(categoria):
    while True:
        try:
            if categoria == "Piscina":
                opcion = int(input("Seleccione una subcategoría:\n1. Terminación\n2. Borde\n"))
                if opcion in [1, 2]:
                    if opcion == 1:
                        return "Terminacion"
                    elif opcion == 2:
                        return "Borde"
                    else:
                        print("Opción no válida. Intente nuevamente.")
            elif categoria == "Revestimiento":
                opcion = int(input("Seleccione una subcategoría:\n1. Piso\n2. Pared\n3. Piso y Pared\n"))
                if opcion in [1, 2, 3]:
                    if opcion == 1:
                        return "Piso"
                    elif opcion == 2:
                        return "Pared"
                    elif opcion == 3:
                        return "Piso y Pared"
                    else:
                        print("Opción no válida. Intente nuevamente.")
            elif categoria == "Adicionales":
                opcion = int(input("Seleccione una subcategoría:\n1. Tuberías de PVC\n2. Skimmers\n3. Desagües\n4. Bomba de agua\n5. Filtro\n6. Clorador\n7. Iluminación\n8. Cableado eléctrico\n9. Escaleras\n"))
                if opcion in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if opcion == 1:
                        return "Tuberías de PVC"
                    elif opcion == 2:
                        return "Skimmers"
                    elif opcion == 3:
                        return "Desagües"
                    elif opcion == 4:
                        return "Bomba de agua"
                    elif opcion == 5:
                        return "Filtro"
                    elif opcion == 6:
                        return "Clorador"
                    elif opcion == 7:
                        return "Iluminación"
                    elif opcion == 8:
                        return "Cableado eléctrico"
                    elif opcion == 9:
                        return "Escaleras"
            else:
                print("Categoría no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

def obtener_tipo_terminacion():
    while True:
        try:
            opcion = int(input("Seleccione el tipo de terminación:\n1. Pintura\n2. Revestimiento\n3. Impermeabilizante\n"))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return "Pintura"
                elif opcion == 2:
                    return "Revestimiento"
                elif opcion == 3:
                    return "Impermeabilizante"
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido (1, 2 o 3).")

def obtener_tipo_borde():
    while True:
        try:
            opcion = int(input("Seleccione el tipo de borde:\n1. Borde ballena\n2. Borde recto\n3. Borde L\n4. Esquina ballena\n5. Esquina recta\n6. Esquina L\n"))
            if opcion in [1, 2, 3, 4, 5, 6]:
                if opcion == 1:
                    return "Borde ballena"
                elif opcion == 2:
                    return "Borde recto"
                elif opcion == 3:
                    return "Borde L"
                elif opcion == 4:
                    return "Esquina ballena"
                elif opcion == 5:
                    return "Esquina recta"
                elif opcion == 6:
                    return "Esquina L"
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido (1 al 6).")

def obtener_tipo_superficie():
    while True:
        try:
            opcion = int(input("Seleccione el tipo de superficie:\n1. Piso\n2. Pared\n3. Piso y Pared\n"))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return "Piso"
                elif opcion == 2:
                    return "Pared"
                elif opcion == 3:
                    return "Piso y Pared"
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido (1, 2 o 3).")

def obtener_ubicacion():
    while True:
        try:
            opcion = int(input("Seleccione la ubicación:\n1. Interior\n2. Exterior\n3. Interior y Exterior\n"))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return "Interior"
                elif opcion == 2:
                    return "Exterior"
                elif opcion == 3:
                    return "Interior y Exterior"
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido (1, 2 o 3).")


def agregar_producto(gestion, opcion):
    try:
        nombre = input('Ingrese el nombre del producto: ')
        id_producto = input('Ingrese el ID del producto: ')# Cambio de nombre de la variable para evitar conflicto con 'id'
        precio = float(input('Ingrese el precio del producto: '))
        stock = int(input('Ingrese la cantidad en stock: '))
        categoria = obtener_categoria()
        subcategoria = obtener_subcategoria(categoria)
        material = input('Ingrese el material del producto: ')
        color = input('Ingrese el color del producto: ')

        if categoria == "Piscina":
            cantidad_unidad_venta = input('A- Ingrese la cantidad y unidad de venta del producto: ')
            if subcategoria.lower().strip() == 'borde':
                tipo_borde = obtener_tipo_borde()
                largo = float(input('Ingrese el largo del producto en cm: '))
                ancho = float(input('Ingrese el ancho del producto en cm: '))
                espesor = float(input('Ingrese el espesor del producto en cm: '))
                producto = ProductoBorde(nombre, id_producto.lower(), precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_borde, largo, ancho, espesor)
                gestion.crear_producto(producto)
                input('Presione Enter para continuar...')
            else:
                if subcategoria.lower().strip() == 'terminacion':
                    tipo_terminacion = obtener_tipo_terminacion()
                    producto = ProductoTerminacion(nombre, id_producto.lower(), precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_terminacion)
                    gestion.crear_producto(producto)
                    input('Presione Enter para continuar...')
        
        elif categoria == "Revestimiento":
            cantidad_unidad_venta = int(input('B- Ingrese la cantidad y unidad de venta del producto: '))
            tipo_superficie = obtener_tipo_superficie()
            ubicacion = obtener_ubicacion()
            largo = float(input('Ingrese el largo del producto en Cm: '))
            ancho = float(input('Ingrese el ancho del productoen Cm: '))
            espesor = float(input('Ingrese el espesor del producto en Cm: '))
            producto = ProductoRevestimiento(nombre, id_producto.lower(), precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_superficie, ubicacion, largo, ancho, espesor)
            gestion.crear_producto(producto)
            input('Presione Enter para continuar...')
        
        elif categoria == "Adicionales":
            uso_funcion = input('C- Ingrese el uso o función del producto: ')
            producto = ProductoAdicionales(nombre, id_producto.lower(), precio, stock, categoria, subcategoria, material, color, uso_funcion )
            gestion.crear_producto(producto)
            input('Presione Enter para continuar...')
    except ValueError as e:
        print(f'Error:', e)
    except Exception as e:
        print(f'Por favor, intente nuevamente')


def buscar_producto_por_nombre(gestion):
    ''' Buscar un producto por nombre'''
    nombre = input('Ingrese el nombre del producto a buscar: ')
    producto = gestion.buscar_producto(nombre)
    if producto:
        print(producto)
    else:
        print(f'El producto {nombre} no se encuentra en el inventario')


def actualizar_producto(gestion):
    ''' Actualizar un producto'''
    nombre = input('Ingrese el nombre del producto a actualizar: ')
    producto = gestion.buscar_producto(nombre)
    if producto:
        print('Producto a actualizar:')
        print(producto)
        print('Ingrese los nuevos datos del producto:')
        datos = agregar_producto()
        gestion.actualizar_producto(nombre, datos)
        print('Producto actualizado correctamente')
    else:
        print(f'El producto {nombre} no se encuentra en el inventario')


def eliminar_producto(gestion):
    ''' Eliminar un producto por nombre'''
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    gestion.eliminar_producto(nombre)
    print(f'Producto {nombre} eliminado correctamente')


def listar_productos(gestion):
    ''' Listar todos los productos'''
    productos = gestion.listar_productos()
    if productos:
        for producto in productos:
            print(producto)
    else:
        print('No hay productos en el inventario')

# Programa principal
if __name__ == "__main__":
    archivo_productos = 'productos_db.json' # Ruta del archivo Json donde se guardan los productos
    gestion_productos = Inventario(archivo_productos)

    # Cargar los productos desde el archivo
    while True: 
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2' or opcion == '3':
            agregar_producto(gestion_productos,opcion)
        elif opcion == '4':
            buscar_producto_por_nombre(gestion_productos)

        elif opcion == '5':
            actualizar_producto(gestion_productos)

        elif opcion == '6':
            eliminar_producto(gestion_productos)

        elif opcion == '7':
            listar_productos(gestion_productos)

        elif opcion == '8':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-8)')
        


# Ejemplo de uso:
# terminacion_ceramica = ProductoTerminacion("Gres porcelánico", 5200, 1000, "Piscina", "Terminación", "Cerámica", "Azul", cantidad_unidad_venta="Una malla de 31 cm x 31 cm x 4 mm, gres Formato:50x50 mm")
# terminacion_mosaico  = ProductoTerminacion("Gres", 6300, 1000, "Piscina","Terminación", "vitrio", "Mar", cantidad_unidad_venta="una malla de 31 cm x 31 cm x 4 mm, gresite Formato: 25x25 mm")
# terminacion_pintura = ProductoTerminacion("Latex Para Piscinas acme", 50, 100, "Piscina", "Terminación", "Pintura latex  base al agua", "Celeste", cantidad_unidad_venta="10L")
# terminacion_Microcemento = ProductoTerminacion("Microcemento X para piscinas", 8000, 1000, "Piscina","Terminación", "cementicio", "blanco", cantidad_unidad_venta="19 kg")
# borde_ballena = ProductoBorde("Arco Romano", 80, 30, "Piscina", "Borde", "Atermico", "Blanco", 50, 30, 1.2, cantidad_unidad_venta="1 baldosa: 50x50 cm x 1.2 cm") 


# revestimiento_piso = ProductoRevestimiento("Florentino", 5200, 1000, "Revestimiento", "Piso","Exterior", "Cementicio", "Negro", 40, 40, 2)
# revestimiento_pared = ProductoRevestimiento("Recubrimiento texturado", 80, 70,"Revestimiento", "Pared","Exterior", "Texturado", "Gris", 220, 17, 1.5)

# tuberias_pvc = ProductoAdicionales("Codo Pvc 50 Mm 90º X", 20, 100, "Adicionales", "Tuberías de PVC")
# skimmers = ProductoAdicionales("Skimmer Boca Ancha Hormigon X Piscina Pileta 38 Cm", 50, 80, "Adicionales", "Skimmers")
# desagues = ProductoAdicionales("Rejilla Pileta De Patio", 30, 60, "Adicionales", "Desagües")
# bomba_agua = ProductoAdicionales("Bomba De Agua Para Pileta - Autocebante", 150, 40,"Adicionales", "Bomba de agua")
# filtro = ProductoAdicionales("Filtro de arena para pileta X", 100, 70, "Adicionales", "Filtro")
# clorador = ProductoAdicionales("Dosificador De Cloro", 80, 50, "Adicionales", "Clorador")
# iluminacion = ProductoAdicionales("Led Rgb Para Pileta 9w", 70, 30, "Adicionales", "Iluminación")
# cableado_electrico = ProductoAdicionales("Cable 4 Hilos Piscina Pileta X1 Metro Mallado 4x0.22", 40, 90, "Adicionales", "Cableado eléctrico")
# escaleras = ProductoAdicionales("Escalera Piscina Pileta X", 120, 20, "Adicionales", "Escaleras")

# Imprimir los productos en formato de diccionario:
# print("Piscina:")
# print(terminacion_ceramica.__str__())
# print(terminacion_mosaico.__str__())
# print(terminacion_pintura.__str__())
# print(terminacion_Microcemento.__str__())
# print(borde_ballena.__str__())
# print()

# print("Revestimiento:")
# print(revestimiento_piso.__str__())
# print(revestimiento_pared.__str__())
# print()

# print("Adicionales:")
# print(tuberias_pvc.__str__())
# print(skimmers.__str__())
# print(desagues.__str__())