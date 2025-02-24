from model.productoTecnologico import ProductoTecnologico


class Celular(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, capacidad):
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.capacidad = capacidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nCapacidad: {self.capacidad}\n"
    
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
    
    