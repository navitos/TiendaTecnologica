from model.productoTecnologico import ProductoTecnologico


class Celular(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, capacidad):
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.capacidad = capacidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nCapacidad: {self.capacidad}\n"