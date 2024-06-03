# Hacer un archivo con las caracteristicas de las prendas y otro archivo con los comandos para poder subir las prendas, modificar sus caracteristicas y borrarlas
# La lista de productos nos conviene tenerlas en la API
# Si, por ejemplo, hacemos una lista con los empleados y su salario conviene hacer una lista vacía a la que le vamos metiendo los empleados de la empresa
# Listas --> plural

from flask import Flask, jsonify, request


class CaracteristicasRopa:

    def _init_(self, nombre, prenda, talle, precio):
        self.nombre = nombre
        self.prenda = prenda
        self.talle = talle
        self.precio = precio


app = Flask(_name_)

precios = {80: "Camisa", 100: "Pantalón de vestir", 120: "saco", 300: "traje completo", 20: "corbata", 250: "vestido",
           150: "falda"}


class Talles():
    talles = ('XS', 'S', 'M', 'L', 'XL', 'XXL')


salir_perfil = False
salir = False
salir2 = False

print("-------------")
print("¿Quieres ingresar a DressCode?")
print("-------------")

while salir == True:  # Interfaz de DressCode
    entrar = int(input("Seleccionar 1 si quieres ingresar: "))
    if entrar == 1:  # Entrar a DressCode

        salir_perfil = True
        print("Entrando a DresCode.....")
        input()
        crear_usuario1 = (input("Ingrese su usuario: "))
        crear_usuario2 = (input("Ingrese su contraseña: "))
        print("Bienvenido a DressCode")

# Ver todo
productos = [
    {'Prenda': 'camisa', 'stock': 5, 'genero': 'hombre'},
    {'Prenda': 'pantalon de vestir', 'stock': 20, 'genero': 'hombre'},
    {'Prenda': 'saco', 'stock': 500, 'genero': 'hombre'},
    {'Prenda': 'traje completo', 'stock': 450, 'genero': 'hombre'},
    {'Prenda': 'corbata', 'stock': 450, 'genero': 'hombre'},
    ##{'Prenda': 'vestido', 'stock': 250,'genero':'mujer'},
    ##{'Prenda': 'falda', 'stock': 150,'genero':'mujer'},
]


# En vez de hacer tres listas distinas, para mi es mejor hacer 1 sola y en la de productos poner de que genero es


# D.32: [GET] Nuestra primera API

#
# D.35: [GET] Consultando información de todos los productos
#
@app.route('/productos', methods=['GET'])
def productosGet():
    return jsonify({'productos': productos, 'status': 'ok'})


#
# D.37: [GET] Consultando información de un único producto
#
@app.route('/productos/<producto>', methods=[
    'GET'])  # En esta linea estamos definiendo cómo queremos que se llame a la variable con el método GET
def productoGet(producto):
    for indice, p in enumerate(productos):
        print(indice, 'indice')
        if p['Prenda'] == producto:
            return jsonify({'producto': productos[indice], 'busqueda': producto, 'status': 'ok'})
    return jsonify({'productos': productos, 'status': 'not found'})


@app.route('/productos/genero/<genero>', methods=[
    'GET'])  # En esta linea estamos definiendo cómo queremos que se llame a la variable con el método GET
def productoGetHombres(genero):
    res = []
    for indice, p in enumerate(productos):
        print(p)
        print(indice)
        if p['genero'] == genero:
            res.append(p)
    if (res == []):
        return jsonify({'productos': 'not found', 'status': 'ok'})
    else:
        return jsonify({'productos': res, 'status': 'ok'})


# D.39: [POST] Dando de alta un nuevo producto
#
@app.route('/productos', methods=['POST'])
def productoPost():
    body = request.json  # request --> forma en la que viaja la informacion a traves de la API
    prenda = body[('Prenda')]
    stock = body['stock']
    genero = body['genero']
    productoAlta = {'Prenda': prenda, 'stock': stock,
                    'genero': genero}  # se crea un diccionario que va a agregar el producto a la lista
    productos.append(productoAlta)
    return jsonify({'productos': productos, 'status': 'ok'})


# A la hora de agregar productos, hay que ponerlos todos en minuscula o todos en mayuscula
#
# D.42: [PUT] Actualiza un Producto
#             - busca por el nombre
#             - y actualiza el stock
#
@app.route('/productos', methods=['PUT'])
def productoPut():
    body = request.json
    nombre = body['Nombre']
    stock = body['stock']  # nuevo stock que actualicé
    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:  # busco el nombre para ver si coincide
            p['stock'] = stock  # actualizacion del stock
            return jsonify({'producto': p,
                            'busqueda': nombre,
                            'status': 'ok'})

    return jsonify({'busqueda': productos,
                    'status': 'not found'})


#
# D.37: [DELETE] Consultando información de un único producto
#
@app.route('/productos/<producto>', methods=[
    'DELETE'])  # <producto> es un PATH Param porque a la hora de borrar el tensiometro yo lo agrego al parametro como parte del path de la url          # a traves del for recorro el diccionario
def productoDelete(producto):
    for indice, p in enumerate(productos):
        if p['Prenda'] == producto:
            productos[indice:indice + 1] = []
            return jsonify({'producto': p, 'busqueda': producto, 'status': 'ok'})
    return jsonify({'productos': productos, 'status': 'nof found'})


# '?' --> Query param --> viaja en la url -->
# '/' -- Path Param --> viaja en la url -->
# raw --> body param --> viaja en el cuerpo


if _name_ == '_main_':
    app.run(debug=True, port=5000)