from abc import ABC, abstractmethod
#Clase abstracta que representa un producto tecnologico, que tiene un nombre, descripcion, precio, stock y marca
class ProductoTecnologico(ABC):
    def __init__(self, nombre, descripcion, precio, stock, marca): #constructor de la clase productoTecnologico, que recibe un nombre, descripcion, precio, stock y marca y los almacena en atributos para su posterior uso
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self.set_precio(precio)
        self.set_stock(stock)
        self.set_marca(marca)

    def __str__(self): #metodo para mostrar el producto en pantalla, que devuelve una cadena de caracteres que representa el producto y sus atributos
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock} \nMarca: {self.marca}"
    
    @abstractmethod
    def get_nombre(self): #metodo para obtener el nombre del producto, que devuelve una cadena de caracteres que representa el nombre
        pass
    
    @abstractmethod
    def get_descripcion(self): #metodo para obtener la descripcion del producto, que devuelve una cadena de caracteres que representa la descripcion
        pass
    
    @abstractmethod
    def get_precio(self): #metodo para obtener el precio del producto, que devuelve un entero que representa el precio
        pass
    
    @abstractmethod
    def get_stock(self): #metodo para obtener el stock del producto, que devuelve un entero que representa el stock
        pass

    @abstractmethod
    def get_marca(self): #metodo para obtener la marca del producto, que devuelve una cadena de caracteres que representa la marca
        pass

    @abstractmethod
    def set_nombre(self, nombre): #metodo para establecer el nombre del producto, que recibe una cadena de caracteres y la almacena en el atributo nombre
        pass

    @abstractmethod
    def set_descripcion(self, descripcion): #metodo para establecer la descripcion del producto, que recibe una cadena de caracteres y la almacena en el atributo descripcion
        pass

    @abstractmethod
    def set_precio(self, precio): #metodo para establecer el precio del producto, que recibe un entero y lo almacena en el atributo precio
        pass

    @abstractmethod
    def set_stock(self, stock): #metodo para establecer el stock del producto, que recibe un entero y lo almacena en el atributo stock
        pass

    @abstractmethod
    def set_marca(self, marca): #metodo para establecer la marca del producto, que recibe un string y lo almacena en el atributo marca
        pass
        
    @abstractmethod
    def calcularPrecio(self): #metodo para calcular el precio del producto, que devuelve un entero que representa el precio
        pass



    
 
  

    

    

