from abc import ABC, abstractmethod

class ProductoTecnologico(ABC):
    def __init__(self, nombre, descripcion, precio, stock, marca):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}"
    
    @abstractmethod
    def get_nombre(self):
        pass
    
    @abstractmethod
    def get_descripcion(self):
        pass
    
    @abstractmethod
    def get_precio(self):
        pass
    
    @abstractmethod
    def get_stock(self):
        pass

    @abstractmethod
    def get_marca(self):
        pass

    @abstractmethod
    def set_nombre(self, nombre):
        pass

    @abstractmethod
    def set_descripcion(self, descripcion):
        pass

    @abstractmethod
    def set_precio(self, precio):
        pass

    @abstractmethod
    def set_stock(self, stock):
        pass


    
 
  

    

    

