from model.celular import Celular
from model.computador import Computador
from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor


class ControladorTienda:
    def __init__(self, productos):
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def mostrar_productos(self):
        print(self.productos)

hola = ControladorTienda([])
hola.agregar_producto(Celular("iphone 13", "celular de 13 megapixels", 1000, 100, "apple", 13))
hola.agregar_producto(Computador("macbook air", "macbook air de 16 gb", 1000, 100, "apple", "rtx 3060", 32,Monitor("apple", 16, 60)))

for producto in hola.productos:
    print(producto.__str__())