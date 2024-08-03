import os
import platform

from laboratorio_Poo import ProductoTerminacion, ProductoBorde, ProductoRevestimiento, ProductoAdicionales

# Ejemplo de uso:
terminacion_ceramica = ProductoTerminacion("Gres porcelánico", 50, 100, "Piscina", "Terminación", "Cerámica", "Azul", cantidad_unidad_venta="malla de 31 cm x 31 cm x 4 mm, gres Formato:50x50 mm")
# terminacion_mosaico  = ProductoTerminacion("Gres", 50, 100, "Piscina","Terminación", "vitrio", "Mar", cantidad_unidad_venta="malla de 31 cm x 31 cm x 4 mm, gresite Formato: 25x25 mm")
# terminacion_pintura = ProductoTerminacion("Latex Para Piscinas X", 50, 100, "Piscina", "Terminación", "Pintura latex  base al agua", "Celeste", cantidad_unidad_venta="10L")
# terminacion_Microcemento = ProductoTerminacion("Microcemento X para piscinas", 50, 100, "Piscina","Terminación", "cementicio", "blanco", cantidad_unidad_venta="19 kg")
# borde_ballena = ProductoBorde("Arco Romano Borde Ballena", 80, 30, "Piscina", "Borde Ballena", "Atermico", "Blanco", 50, 30, 1.2, cantidad_unidad_venta="1 baldosa: 50x50 cm x 1.2 cm") 


# revestimiento_piso = ProductoRevestimiento("Baldosas de cerámica", 50, 100, "Revestimiento", "Piso","Interior", "Cerámica", "Blanco", 60, 30, 1.2)
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
print("Piscina:")
print(terminacion_ceramica.__str__())
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