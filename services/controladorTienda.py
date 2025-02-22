class ControladorTienda:
    def __init__(self, productos):
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def mostrar_productos(self):
        print(self.productos)