from model.productoTecnologico import ProductoTecnologico

#Clase hija de productoTecnologico que representa un celular, que tiene un nombre, descripcion, precio, stock, marca, capacidad y fechaLanzamiento
class Celular(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento): #metodo para crear un celular, que recibe un nombre, descripcion, precio, stock, marca, capacidad y fechaLanzamiento y los almacena en atributos instanciando un celular
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.set_capacidad(capacidad)
        self.set_fechaLanzamiento(fechaLanzamiento)

    def __str__(self): #metodo para mostrar el celular en pantalla, que devuelve una cadena de caracteres que representa el celular y sus atributos
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nCapacidad: {self.capacidad}\nFecha de lanzamiento: {self.fechaLanzamiento}\n"
    
    def get_nombre(self): #metodo para obtener el nombre del celular, que devuelve una cadena de caracteres que representa el nombre del celular
        return self.nombre
    
    def get_descripcion(self): #metodo para obtener la descripcion del celular, que devuelve una cadena de caracteres que representa la descripcion del celular
        return self.descripcion
    
    def get_precio(self): #metodo para obtener el precio del celular, que devuelve un double que representa el precio del celular
        return self.precio
    
    def get_stock(self): #metodo para obtener el stock del celular, que devuelve un entero que representa el stock del celular
        return self.stock
    
    def get_marca(self): #metodo para obtener la marca del celular, que devuelve una cadena de caracteres que representa la marca del celular
        return self.marca
    
    def get_capacidad(self): #metodo para obtener la capacidad del celular, que devuelve un double que representa la capacidad del celular
        return self.capacidad
    
    def get_fechaLanzamiento(self): #metodo para obtener la fecha de lanzamiento del celular, que devuelve una fecha que representa la fecha de lanzamiento del celular
        return self.fechaLanzamiento
    
    def set_marca(self, marca): #metodo para establecer la marca del celular, que recibe una cadena de caracteres y la almacena en el atributo marca
        self.marca = marca
        
    def set_capacidad(self, capacidad): #metodo para establecer la capacidad del celular, que recibe un double y lo almacena en el atributo capacidad
        self.capacidad = capacidad
        
    def set_fechaLanzamiento(self, fechaLanzamiento): #metodo para establecer la fecha de lanzamiento del celular, que recibe una fecha y la almacena en el atributo fechaLanzamiento
        self.fechaLanzamiento = fechaLanzamiento
    
    def set_descripcion(self, descripcion): #metodo para establecer la descripcion del celular, que recibe una cadena de caracteres y la almacena en el atributo descripcion
        self.descripcion = descripcion
        
    def set_precio(self, precio): #metodo para establecer el precio del celular, que recibe un double y lo almacena en el atributo precio
        self.precio = precio
        
    def set_stock(self, stock): #metodo para establecer el stock del celular, que recibe un entero y lo almacena en el atributo stock
        self.stock = stock
    
    def set_nombre(self, nombre): #metodo para establecer el nombre del celular, que recibe una cadena de caracteres y la almacena en el atributo nombre
        self.nombre = nombre
    
    def calcularPrecio(self): #metodo para calcular el precio del celular, que devuelve un double que representa el precio del celular
        return self.precio + self.precio * 0.19
    
