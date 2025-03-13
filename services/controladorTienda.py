from model.celular import Celular
from model.computador import Computador
from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor
from services.observable import Observable

#Clase que controla la tienda tecnologica
class ControladorTienda:
    def __init__(self, productos): #constructor de la clase controladorTienda
        self.productos = productos
        self.observable = Observable()

    def agregar_celular(self, nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento): #metodo para agregar un celular a la tienda, que recibe los atributos del celular y lo agrega a la lista
        try:
            celular = Celular(nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento)
            self.productos.append(celular)
        except ValueError as e:
            print(e)
        
    def agregar_computador(self, nombre, descripcion, precio, stock, marca, grafica, ram): #metodo para agregar un computador a la tienda, que recibe los atributos del computador, crea el computador y finalmente lo agrega
        try:
           computador = Computador(nombre, descripcion, precio, stock, marca, grafica, ram, Monitor("generico", 15, 60)) 
           self.productos.append(computador)
        except ValueError as e:
           print(e)   

    def eliminar_producto(self, producto): #metodo para eliminar un producto de la tienda, que elimina el producto de la lista
        self.productos.remove(producto)

    def mostrar_productos(self): #metodo para mostrar todos los productos de la tienda, que devuelve una lista de productos
        for producto in self.productos:
            print(producto.__str__())
    
    def listar_celulares(self): #metodo para listar todos los celulares de la tienda, que devuelve una lista de celulares
        for celular in self.productos:
            if isinstance(celular, Celular):
                print(celular.__str__())
    
    def listar_computadores(self): #metodo para listar todos los computadores de la tienda, que devuelve una lista de computadores
        for computador in self.productos:
            if isinstance(computador, Computador):
                print(computador.__str__())

    def get_producto(self, index): #metodo para mostrar un producto en especifico de la tienda, que devuelve el producto buscado
        print(self.productos[index].__str__())
    
    def buscar_producto(self, nombre): #metodo para buscar un producto en la tienda, que devuelve el producto buscado
        for i in self.productos:
            if i.get_nombre() == nombre:
                return i
        return None
    
    def calcular_total(self): #metodo para calcular el total de todos los productos de la tienda, que devuelve el total de precio de todos los productos
        total = 0
        for i in self.productos:
            total += i.calcularPrecio() * i.get_stock()
        return total

    def calcular_total_celulares(self): #Metodo para calcular el total de precio de todos los celulares de la tienda, que devuelve el total de precio de todos los celulares
        total = 0
        for i in self.productos:
            if isinstance(i, Celular):
                total += i.calcularPrecio() * i.get_stock()
        return total
    
    def calcular_total_computadores(self): #Metodo para calcular el total de precio de todos los computadores de la tienda, que devuelve el total de precio de todos los computadores
        total = 0
        for i in self.productos:
            if isinstance(i, Computador):
                total += i.calcularPrecio() * i.get_stock()
        return total


