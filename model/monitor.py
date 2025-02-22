class Monitor:
    def __init__(self, marca, tamanio, frecuencia):
        self.marca = marca
        self.tamanio = tamanio
        self.frecuencia = frecuencia

    def __str__(self):        
        return f"Marca: {self.marca} Tamanio: {self.tamanio} Frecuencia: {self.frecuencia}"