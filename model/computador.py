from model.productoTecnologico import ProductoTecnologico
from model.monitor import Monitor

#Clase hija de productoTecnologico que representa un computador, que tiene un nombre, descripcion, precio, stock, marca, grafica, ram y monitor
class Computador(ProductoTecnologico):
    def __init__(self, nombre, descripcion, precio, stock, marca, grafica, ram, monitor): #metodo para crear un computador, que recibe un nombre, descripcion, precio, stock, marca, grafica, ram y monitor y los almacena en atributos instanciando un computador
        super().__init__(nombre, descripcion, precio, stock, marca)
        self.set_grafica(grafica)
        self.set_ram(ram)
        self.set_monitor(monitor)

    def __str__(self): #metodo para mostrar el computador en pantalla, que devuelve una cadena de caracteres que representa el computador y sus atributos
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}\nGrafica: {self.procesador}\nMemoria: {self.memoria}\nMonitor: {self.monitor}\n"
    
    def get_nombre(self): #metodo para obtener el nombre del computador, que devuelve una cadena de caracteres que representa el nombre del computador
        return self.nombre
        
    def get_descripcion(self): #metodo para obtener la descripcion del computador, que devuelve una cadena de caracteres que representa la descripcion del computador
        return self.descripcion
        
    def get_precio(self): #metodo para obtener el precio del computador, que devuelve un entero que representa el precio del computador
        return self.precio
        
    def get_stock(self): #metodo para obtener el stock del computador, que devuelve un entero que representa el stock del computador
        return self.stock
        
    def get_marca(self): #metodo para obtener la marca del computador, que devuelve una cadena de caracteres que representa la marca del computador
        return self.marca
        
    def get_grafica(self): #metodo para obtener el grafica del computador, que devuelve una cadena de caracteres que representa el grafica del computador
        return self.procesador
        
    def get_ram(self): #metodo para obtener la memoria del computador, que devuelve un double que representa la memoria del computador
        return self.memoria
        
    def get_monitor(self): #metodo para obtener el monitor del computador, que devuelve un objeto de la clase monitor que representa el monitor del computador
        return self.monitor
    
    def set_grafica(self, grafica): #metodo para establecer el grafica del computador, que recibe una cadena de caracteres y la almacena en el atributo grafica
        self.procesador = grafica
    
    def set_ram(self, ram): #metodo para establecer la memoria del computador, que recibe un double y lo almacena en el atributo memoria
        if ram <= 0:
            raise ValueError("La ram no puede ser menor o igual a 0")
        self.memoria = ram
    
    def set_monitor(self, monitor): #metodo para establecer el monitor del computador, que recibe un objeto de la clase monitor y lo almacena en el atributo monitor
        self.monitor = monitor

    def set_marca(self, marca): #metodo para establecer la marca del computador, que recibe una cadena de caracteres y la almacena en el atributo marca
        self.marca = marca

    def set_descripcion(self, descripcion): #metodo para establecer la descripcion del computador, que recibe una cadena de caracteres y la almacena en el atributo descripcion
        self.descripcion = descripcion

    def set_precio(self, precio): #metodo para establecer el precio del computador, que recibe un entero y lo almacena en el atributo precio
        if precio <= 0:
            raise ValueError("el precio no puede ser negativo o igual a 0")
        self.precio = precio

    def set_stock(self, stock): #metodo para establecer el stock del computador, que recibe un entero y lo almacena en el atributo stock
        if stock < 0:
            raise ValueError("no puede haber valores negativos en la cantidad de inventario 'stock' ")
        self.stock = stock
    
    def set_nombre(self, nombre): #metodo para establecer el nombre del computador, que recibe una cadena de caracteres y la almacena en el atributo nombre
        self.nombre = nombre

    def calcularPrecio(self): #metodo para calcular el precio del computador, que devuelve un double que representa el precio del computador
        return self.precio + self.precio * 0.25
    