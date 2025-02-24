
#Clase que representa un monitor, que tiene una marca, tamanio y frecuencia
class Monitor:
    def __init__(self, marca, tamanio, frecuencia): #constructor de la clase monitor, que recibe una marca, tamanio y frecuencia y los almacena en atributos para su posterior uso
        self.set_marca(marca)
        self.set_tamanio(tamanio)
        self.set_frecuencia(frecuencia)

    def __str__(self):  #metodo para mostrar el monitor en pantalla, que devuelve una cadena de caracteres que representa el monitor y sus atributos
        return f"Marca: {self.marca} Tamanio: {self.tamanio} Frecuencia: {self.frecuencia}"
    
    def get_marca(self): #metodo para obtener la marca del monitor, que devuelve una cadena de caracteres que representa la marca
        return self.marca
        
    def get_tamanio(self): #metodo para obtener el tamanio del monitor, que devuelve un entero que representa el tamanio
        return self.tamanio
        
    def get_frecuencia(self): #metodo para obtener la frecuencia del monitor, que devuelve un entero que representa la frecuencia
        return self.frecuencia
    
    def set_marca(self, marca): #metodo para establecer la marca del monitor, que recibe una cadena de caracteres y la almacena en el atributo marca
        self.marca = marca

    def set_tamanio(self, tamanio): #metodo para establecer el tamanio del monitor, que recibe un entero y lo almacena en el atributo tamanio
        self.tamanio = tamanio

    def set_frecuencia(self, frecuencia): #metodo para establecer la frecuencia del monitor, que recibe un entero y lo almacena en el atributo frecuencia
        self.frecuencia = frecuencia
