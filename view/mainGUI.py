from tkinter import Tk, Frame, Button, Menu
from view.formularioCelular import FormularioCelular
from view.formularioComputador import FormularioComputador
from view.ventanaListar import VentanaListar
from view.ventanaAcerca import VentanaAcerca
from view.ventanaPrecioComputadores import VentanaPrecioComputadores
from view.ventanaPrecioCelulares import VentanaPrecioCelulares
from services.controladorTienda import ControladorTienda
from view.ventanaPrecio import VentanaPrecio
from model.celular import Celular
from model.computador import Computador
from model.monitor import Monitor
from random import choice, randint

class TiendaApp: #Clase que controla la ventana principal de la tienda
    def __init__(self, root): #constructor de la clase TiendaApp
        self.root = root
        self.root.title("Tienda Tecnologica")
        self.root.minsize(width=1000, height=600) # Tamaño mínimo de la ventana
        self.root.resizable(True, True)  # Hacerla redimensionable
        self.centrar_ventana(self.root)  # Centrar la ventana principal

        self.frame_botones = Frame(self.root)
        self.frame_botones.grid(row=0, column=0, sticky="nw")

        self.crear_menus()
        self.crear_botones()
        self.servidor = ControladorTienda([])

        # Generar datos de prueba
        self.generar_datos_prueba()
    
    def crear_menus(self): #metodo para crear los menus de la ventana principal
        self.menu_celular = Menu(self.root, tearoff=0)
        self.menu_celular.add_command(label="Añadir celular", command=self.abrir_ventana_celular)
        self.menu_celular.add_command(label="Consultar celular")
        self.menu_celular.add_command(label="Eliminar celular")
        self.menu_celular.add_command(label="calcular precio", command=self.abrir_ventana_precio_celulares)

        self.menu_computador = Menu(self.root, tearoff=0)
        self.menu_computador.add_command(label="Añadir computador", command=self.abrir_ventana_computador)
        self.menu_computador.add_command(label="Consultar computador")
        self.menu_computador.add_command(label="Eliminar computador")
        self.menu_computador.add_command(label="calcular precio", command=self.abrir_ventana_precio_computadores)


    def crear_botones(self): #metodo para crear los botones de la ventana principal
        self.btn_celular = Button(self.frame_botones, text="Celular", 
                                  command=lambda: self.mostrar_menu_bajo_boton(self.btn_celular, self.menu_celular))
        self.btn_celular.grid(row=0, column=0, sticky="w")

        self.btn_computador = Button(self.frame_botones, text="Computador", 
                                     command=lambda: self.mostrar_menu_bajo_boton(self.btn_computador, self.menu_computador))
        self.btn_computador.grid(row=0, column=1, sticky="w")

        self.btn_listar = Button(self.frame_botones, text="Listar", command=self.abrir_ventana_listar)
        self.btn_calcular = Button(self.frame_botones, text="Calcular Precio", command = self.abrir_ventana_precio)
        self.btn_acerca = Button(self.frame_botones, text="Acerca de", command=self.abrir_ventana_acerca)

        self.btn_listar.grid(row=0, column=2, sticky="w")
        self.btn_calcular.grid(row=0, column=3, sticky="w")
        self.btn_acerca.grid(row=0, column=4, sticky="w")
    
    def mostrar_menu_bajo_boton(self, boton, menu): #metodo para mostrar un menu bajo un boton
        x = boton.winfo_rootx()
        y = boton.winfo_rooty() + boton.winfo_height()
        menu.tk_popup(x, y)

    def abrir_ventana_acerca(self): #metodo para abrir la ventana acerca de
        VentanaAcerca(self.root)

    def abrir_ventana_precio(self): #metodo para abrir la ventana de precio
        VentanaPrecio(self.root, self.servidor)
    
    def abrir_ventana_celular(self): #metodo para abrir la ventana de celular
        FormularioCelular(self.root, self.servidor)

    def abrir_ventana_computador(self): #metodo para abrir la ventana de computador
        FormularioComputador(self.root, self.servidor)

    def abrir_ventana_listar(self): #metodo para abrir la ventana de listar
        VentanaListar(self.root, self.servidor)

    def abrir_ventana_precio_computadores(self): #metodo para abrir la ventana de precio de computadores
        VentanaPrecioComputadores(self.root, self.servidor)
        
    def abrir_ventana_precio_celulares(self): #metodo para abrir la ventana de precio de celulares
        VentanaPrecioCelulares(self.root, self.servidor)
    
    def generar_datos_prueba(self): #metodo para generar datos de prueba para la tienda
        nombres_celulares = ["iPhone 13", "Samsung Galaxy S21", "Google Pixel 6", "Xiaomi Mi 11", "OnePlus 9"]
        nombres_computadores = ["MacBook Pro", "Dell XPS 13", "HP Spectre x360", "Lenovo ThinkPad X1", "Asus ROG Zephyrus"]
        marcas = ["Apple", "Samsung", "Google", "Xiaomi", "Dell", "HP", "Lenovo", "Asus"]
        capacidades = [64, 128, 256, 512, 1024]
        fechas_lanzamiento = ["2021-09-14", "2021-01-29", "2020-10-05", "2022-03-08", "2021-11-15"]

        # Generar 10 celulares de prueba
        for _ in range(10):
            nombre = choice(nombres_celulares)
            descripcion = f"Smartphone de {nombre.split()[0]}"
            precio = randint(500, 1500)
            stock = randint(1, 20)
            marca = choice(marcas)
            capacidad = choice(capacidades)
            fechaLanzamiento = choice(fechas_lanzamiento)
            self.servidor.agregar_celular(nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento)

        # Generar 10 computadores de prueba
        for _ in range(10):
            nombre = choice(nombres_computadores)
            descripcion = f"Laptop de {nombre.split()[0]}"
            precio = randint(800, 3000)
            stock = randint(1, 15)
            marca = choice(marcas)
            grafica = "Integrada" if randint(0, 1) else "Dedicada"
            ram = choice([8, 16, 32])

            self.servidor.agregar_computador(nombre, descripcion, precio, stock, marca, grafica, ram)

    def centrar_ventana(self, ventana): #metodo para centrar la ventana respecto a la pantalla
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

if __name__ == "__main__": #metodo main para correr la aplicacion
    root = Tk()
    app = TiendaApp(root)
    root.mainloop()