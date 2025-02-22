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
    