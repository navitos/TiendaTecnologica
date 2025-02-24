from model.celular import Celular
from model.computador import Computador
from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor

#Clase que controla la tienda tecnologica
class ControladorTienda:
    def __init__(self, productos): #constructor de la clase controladorTienda
        self.productos = productos

    def agregar_celular(self, nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento): #metodo para agregar un celular a la tienda, que recibe los atributos del celular y lo agrega a la lista
        try:
            celular = Celular(nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento)
            self.productos.append(celular)
        except ValueError as e:
            print(e)
        
    def agregar_computador(self, nombre, descripcion, precio, stock, marca, grafica, ram):
        try:
           computador = Computador(nombre, descripcion, precio, stock, marca, grafica, ram, Monitor("generico", 15, 60)) 
           self.productos.append(computador)
        except ValueError as e:
           print(e)   

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
hola.agregar_celular("iphone 13", "celular de 13 megapixels", 1000, 100, "apple", -4, "12/28/2003")
hola.agregar_celular("infinix gt 20 pro", "celular gamer gama alta", 2000, 23, "infinix", 256, "06/06/2024" )
hola.agregar_computador("asus pc", "computador de mesa asus basico", 0,10,"asus","gt1030",8)


for producto in hola.productos:
    print(producto.__str__())