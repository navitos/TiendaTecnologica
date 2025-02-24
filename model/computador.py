from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor


class Computador(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, grafica, ram, monitor):
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.procesador = grafica
        self.memoria = ram
        self.monitor = monitor

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nGrafica: {self.procesador}\nMemoria: {self.memoria}\nMonitor: {self.monitor}\n"
    
    def get_nombre(self):
        return self.nombre
        
    def get_descripcion(self):
        return self.descripcion
        
    def get_precio(self):
        return self.precio
        
    def get_stock(self):
        return self.stock
        
    def get_marca(self):
        return self.marca
        
    def get_grafica(self):
        return self.procesador
        
    def get_ram(self):
        return self.memoria
        
    def get_monitor(self):
        return self.monitor
    
    def set_grafica(self, grafica):
        self.procesador = grafica
    
    def set_ram(self, ram):
        self.memoria = ram
    
    def set_monitor(self, monitor):
        self.monitor = monitor

    def set_marca(self, marca):
        self.marca = marca

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_precio(self, precio):
        self.precio = precio

    def set_stock(self, stock):
        self.stock = stock
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    