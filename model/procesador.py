class Procesador:
    def __init__(self, marca, velocidad, nucleos):
        self.marca = marca
        self.velocidad = velocidad
        self.nucleos = nucleos

    def __str__(self):
        return f"Marca: {self.marca}\nVelocidad: {self.velocidad}\nNucleos: {self.nucleos}"