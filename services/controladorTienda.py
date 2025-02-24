from model.celular import Celular
from model.computador import Computador
from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor

#Clase que controla la tienda tecnologica
class ControladorTienda:
    def __init__(self, productos): #constructor de la clase controladorTienda
        self.productos = productos

    def agregar_producto(self, producto): #metodo para agregar un producto a la tienda, que recibe un producto y lo agrega a la lista
        self.productos.append(producto)

    def eliminar_producto(self, producto): #metodo para eliminar un producto de la tienda, que elimina el producto de la lista
        self.productos.remove(producto)

    def mostrar_productos(self): #metodo para mostrar todos los productos de la tienda, que devuelve una lista de productos
        print(self.productos)

    def buscar_producto(self, producto): #metodo para buscar un producto en la tienda, que devuelve el producto buscado
        for i in self.productos:
            if i.get_nombre() == producto:
                return i
        return None
    
    def calcular_total(self): #metodo para calcular el total de todos los productos de la tienda, que devuelve el total
        total = 0
        for i in self.productos:
            total += i.calcularPrecio()
        return total


#prueba en consola del funcionamiento del controlador y las clases basicas
hola = ControladorTienda([])
hola.agregar_producto(Celular("iphone 13", "celular de 13 megapixels", 1000, 100, "apple", 13))
hola.agregar_producto(Computador("macbook air", "macbook air de 16 gb", 1000, 100, "apple", "rtx 3060", 32,Monitor("apple", 16, 60)))

for producto in hola.productos:
    print(producto.__str__())