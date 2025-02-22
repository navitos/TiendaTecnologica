from model import productoTecnologico


class Computador(productoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, procesador, memoria, grafico, teclado, mouse):
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.procesador = procesador
        self.memoria = memoria
        self.grafico = grafico
        self.teclado = teclado
        self.mouse = mouse

    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nProcesador: {self.procesador}\nMemoria: {self.memoria}\nGrafico: {self.grafico}\nTeclado: {self.teclado}\nMouse: {self.mouse}"
    