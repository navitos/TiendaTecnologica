class Monitor:
    def __init__(self, marca, tamanio, frecuencia):
        self.marca = marca
        self.tamanio = tamanio
        self.frecuencia = frecuencia

    def __str__(self):        
        return f"Marca: {self.marca} Tamanio: {self.tamanio} Frecuencia: {self.frecuencia}"
    
    def get_marca(self):
        return self.marca
        
    def get_tamanio(self):
        return self.tamanio
        
    def get_frecuencia(self):
        return self.frecuencia
    
    def set_marca(self, marca):
        self.marca = marca

    def set_tamanio(self, tamanio):
        self.tamanio = tamanio

    def set_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia