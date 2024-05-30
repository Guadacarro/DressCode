##Atributos:
# id: Identificador único de la prenda (autogenerado)
# sexo: "Hombre" o "Mujer"
# categoria: "Formal", "Urbano", "Fitness", "Outdoor" o "Vintage/Retro"
# unisex
# nombre: Nombre de la prenda
# precio: Precio unitario de la prenda
# talles: Diccionario donde la clave es la talla (XS, S, M, L, XXL) y el valor es la cantidad disponible en esa talla

# Métodos:
# init(self, tipo, categoria, nombre, descripcion, precio, talles): Constructor de la clase.
# descontar_stock(self, talla, cantidad): Decrementa la cantidad disponible de una talla específica.
# Pedido:

# Atributos:
# prendas: Lista de objetos de tipo Prenda con la cantidad deseada de cada uno
# email_cliente: Correo electrónico del cliente
# metodo_pago: Método de pago elegido por el cliente ("Tarjeta de crédito", "Efectivo", etc.)
# total: Precio total del pedido (suma del precio de cada prenda * cantidad)
# Métodos:
# init(self, prendas, email_cliente, direccion_entrega, metodo_pago): Constructor de la clase.
# calcular_total(self): Calcula el precio total del pedido.
# Tienda:
# EJEMPLO --> GET que me traiga ropa de temporada de invierno, GET que me traiga ropa con detalles

# Atributos:
# prendas: Lista de objetos de tipo Prenda
# pedidos: Lista de objetos de tipo Pedido
# Métodos:
# init(self): Constructor de la clase.
# agregar_prenda(self, prenda): Agrega una nueva prenda a la tienda.
# obtener_prenda(self, id_prenda): Obtiene una prenda por su ID.
# buscar_prendas(self, tipo, categoria, nombre): Busca prendas por tipo, categoría y nombre.
# obtener_pedido(self, id_pedido): Obtiene un pedido por su ID.
# Funciones:

# cargar_datos(tienda): Carga los datos de las prendas y pedidos desde un archivo (por ejemplo, JSON, CSV) a la tienda.
# guardar_datos(tienda): Guarda los datos de las prendas y pedidos de la tienda a un archivo.

# Agregar prendas -->listar prenda de invierno, listar prenda de verano
# Eliminar prendas -->
# Hacer codigo que escribe contra una base de datos
# Haces una API

import os

genero = {1: "Hombre", 2: "Mujer", 3: "Ver todo"}

formal_hombre = {1: "camisa", 2: "pantalón de vestir", 3: "saco", 4: "traje completo", 5: "Corbata"}
formal_mujer = {1: "vestido", 2: "falda"}
formal_todo = {1: "Camisa", 2: "Pantalón de vestir", 3: "saco", 4: "traje completo", 5: "corbata", 6: "vestido",
               7: "falda"}

precios = {'Formal': 150, 'Urbano': 70, 'Fitness': 50, 'Outdoor': 120, 'Vintage/Retro': 100}


class PrendaFormal():
    talles = ('XS', 'S', 'M', 'L', 'XL', 'XXL')


class Persona:

    def __init__(self, nombre, prenda, categoria, precio):
        self.nombre = nombre
        self.prenda = prenda
        self.categoria = categoria
        self.prenda = categoria
        self.precio = precio


class Camisadejuan():
    nombre = 'Juan'
    prenda = 'camisa'
    categoria = 'Formal'
    talle = 'L'
    precio = '150'


aumento_porcentual = float(input("¿Cuánto desea modificar el precio?"))


def actualizar_precio():
    porcentaje_de_aumento_de_precio = aumento_porcentual
    actualizar_precio = precio * aumento_porcentual + precio


# def __init__(nombre,categoria,talle,precio):
#    self.nombre =
#    self.categoria =


# Pensar que las caracteristicas se pueden poner como atributos
# Clase --> camisa en particular # Camisa de algodón talle 41
# Atributos --> camisa, pulover, remera, talle,precio
# Método --> cambiar precio, cambiar stock
# Ejemplo --> método que le cambie el precio a un producto
# Objeto --> camisa cuadros

# Qué clase vamos a usar y qué métodos vamos a usar
correos_de_usuarios = {}
talle = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "XL", 6: "XXL"}

metodo_de_pago = {1: "Mercado pago", 2: "Tarjeta de débito", 3: "Tarjeta de crédito", 4: "Efectivo"}

import os

print("-------------")
print("¿Quieres ingresar a la API de Dress Code?")
print("-------------")

crear_usuario1 = (input("Ingrese su usuario: "))
crear_usuario2 = (input("Ingrese su contraseña: "))
precio_nuevo = (input("¿Cuánto desea ac: "))
cambio_de_precio = precio_nuevo

salir_perfil = False
salir = False
salir2 = False

while salir == True:  # Interfaz de DressCode
    entrar = int(input("Seleccionar 1 si quieres ingresar: "))
    if entrar == 1:  # Entras a DressCode

        print("Entrando a Dress Code.....")

        crear_usuario1 = (input("Ingrese su usuario: "))
        crear_usuario2 = (input("Ingrese su contraseña: "))
        print("Bienvenido a DressCode")

    while salir2 == True:
        comandos = int(input('Ingrese la opcion deseada:'))
        print('\t 1: AGREGAR PRENDA')
        print('\t 2: MODIFICAR PRECIO')
        print('\t 2: MODIFICAR STOCK')
        print('\t 3: MODIFICAR PRECIO')
        print('\t 4: SALIR')
    break  # Pongo el break para que una vez que se ingresen los datos se corte el programa #Esto está como parche temporal hasta que le metamos mas codigo

# print ('Ingrese la opcion deseada:')
#    print ('\t 1: AGREGAR PRENDA')
#    print ('\t 2: MODIFICAR PRECIO')
#    print('\t 2: MODIFICAR STOCK')
#    print('\t 3: MODIFICAR PRECIO')
#    print ('\t 4: SALIR')

# print("Ingrese la opción deseada: ")
# print("\t 1: Hombre")
# print("\t 2 Mujer")
# print("\t 3: Ver todo")


# Cargar datos de la tienda
# tienda = Tienda()
# cargar_datos(tienda)

# Seleccionar una prenda y agregarla al carrito
# prenda_seleccionada = tienda.obtener_prenda(prendas_encontradas[0].id)
# carrito = [{"prenda": prenda_seleccionada, "talle": "M", "cantidad": 1}]

# Crear un pedido y completar los datos del cliente
# pedido = tienda.crear_pedido(carrito, "usuario@ejemplo.com", "Calle 123", "Ciudad,", "Tarjeta de crédito")

# Confirmar y enviar el pedido
# tienda.confirmar_pedido(pedido.id)
# tienda.enviar_pedido(pedido.id)

# Buscar prendas de tipo "Urbano" para mujer
# prendas_encontradas = buscar_prendas(tipo="Urbano", genero="Mujer")

# Obtener detalles de una prenda específica
# prenda_seleccionada = obtener_detalles_prenda(id_prenda=123)

# Agregar la prenda seleccionada al carrito en talle M y cantidad 2
# agregar_prenda_carrito(prenda_seleccionada, "M", 2)

# Crear pedido con la información del usuario y las prendas del carrito
# usuario = Usuario(nombre="Juan Perez", email="juanperez@email.com", domicilio="Calle 123,", metodoPago="Tarjeta de crédito")
# pedido = crear_pedido(usuario, prendas_carrito)

# Imprimir el total del pedido
# print(f"Total del pedido: {pedido.total}")

categoria_ropa = ["Formal"]
print(categoria_ropa)
talle_ropa = ("XS", "S", "M", "L", "XL", "XXL")
print(talle_ropa)

# class Prenda:
#    def __int__(self, tipo, talle, color, material, precio,categoria):
#        self.tipo= tipo
#        self.color=color
#        self.material=material
#        self.precio=precio
#        if talle not in talle_ropa:
#            raise Exception ("Debe ingresar un talle disponible")
#        if categoria not in categoria_ropa:
#            raise Exception ("Debe ingresar una categoría correcta")
#        self.categoria=categoria
#    def Cambiar_precio(self,precio):
#
#    def Modificar_stock(self,stock):
#
#    def __str__(self):
#        return(f"Tipo de ropa: {self.tipo}\nTalle: {self.talle}\nColor:{self.color}\nMaterial:{self.material}\nPrecio:{self.precio}\nCategoría:{self.categoria}")





