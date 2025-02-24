from model.productoTecnologico import ProductoTecnologico


class Celular(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento):
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.capacidad = capacidad
        self.fechaLanzamiento = fechaLanzamiento

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nCapacidad: {self.capacidad}\nFecha de lanzamiento: {self.fechaLanzamiento}\n"
    
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
    
    def get_capacidad(self):
        return self.capacidad
    
    def get_fechaLanzamiento(self):
        return self.fechaLanzamiento
    
    def set_marca(self, marca):
        self.marca = marca
        
    def set_capacidad(self, capacidad):
        self.capacidad = capacidad
        
    def set_fechaLanzamiento(self, fechaLanzamiento):
        self.fechaLanzamiento = fechaLanzamiento
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
        
    def set_precio(self, precio):
        self.precio = precio
        
    def set_stock(self, stock):
        self.stock = stock
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def calcularPrecio(self):
        return self.precio + self.precio * 0.19
    
