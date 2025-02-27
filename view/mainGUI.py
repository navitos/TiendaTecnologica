from tkinter import Tk, Frame, Button, Menu, PhotoImage, Label
from tkinter import ttk
from view.formularioCelular import FormularioCelular
from view.formularioComputador import FormularioComputador
from view.ventanaListar import VentanaListar
from view.ventanaAcerca import VentanaAcerca
from view.ventanaPrecioComputadores import VentanaPrecioComputadores
from view.ventanaPrecioCelulares import VentanaPrecioCelulares
from services.controladorTienda import ControladorTienda
from view.ventanaPrecio import VentanaPrecio
from view.vetanaBuscarCelular import VentanaBuscarCelular
from view.ventanaBuscarComputador import VentanaBuscarComputador
from view.ventanaEliminarCelular import VentanaEliminarCelular
from view.ventanaEliminarComputador import VentanaEliminarComputador
from model.celular import Celular
from model.computador import Computador
from model.monitor import Monitor
from random import choice, randint
from PIL import Image, ImageTk  # Asegúrate de tener instalada la librería Pillow

class TiendaApp: #Clase que controla la ventana principal de la tienda
    def __init__(self, root): #constructor de la clase TiendaApp
        
        self.root = root
        self.root.title("Tienda Tecnologica")
        self.root.minsize(width=1000, height=600) # Tamaño mínimo de la ventana
        self.root.resizable(True, True)  # Hacerla redimensionable
        self.centrar_ventana(self.root)  # Centrar la ventana principal
        self.root.configure(bg="#E3F2FD")  # Fondo azul claro

        # Aplicar la fuente global Poppins
        self.root.option_add("*Font", "Poppins 9")
        self.root.option_add("*Label.Font", "Poppins 9 bold")
        self.root.option_add("*Button.Font", "Poppins 9 bold")

        self.frame_botones = Frame(self.root)
        self.frame_botones.grid(row=0, column=0, sticky="nw")

        self.crear_menus()
        self.cargar_iconos()
        self.crear_botones()
        self.servidor = ControladorTienda([])

        # Generar datos de prueba
        self.generar_datos_prueba()
    
    def crear_menus(self): #metodo para crear los menus de la ventana principal
        self.menu_celular = Menu(self.root, tearoff=0)
        self.menu_celular.add_command(label="Añadir celular", command=self.abrir_ventana_celular)
        self.menu_celular.add_command(label="Consultar celular", command=self.abrir_ventana_buscar_celular)
        self.menu_celular.add_command(label="Eliminar celular", command=self.abrir_ventana_eliminar_celular)
        self.menu_celular.add_command(label="calcular precio", command=self.abrir_ventana_precio_celulares)

        self.menu_computador = Menu(self.root, tearoff=0)
        self.menu_computador.add_command(label="Añadir computador", command=self.abrir_ventana_computador)
        self.menu_computador.add_command(label="Consultar computador", command=self.abrir_ventana_buscar_computador)
        self.menu_computador.add_command(label="Eliminar computador", command=self.abrir_ventana_eliminar_computador)
        self.menu_computador.add_command(label="calcular precio", command=self.abrir_ventana_precio_computadores)
    

    def cargar_iconos(self):
        imagen_calculadora = Image.open("view/resources/calculadora.png")
        imagen_redimensionada1 = imagen_calculadora.resize((25, 25), Image.LANCZOS)  # Ajusta el tamaño según sea necesario
        self.icono_calculadora = ImageTk.PhotoImage(imagen_redimensionada1)

        imagen_lista = Image.open("view/resources/lista.png")
        imagen_redimensionada2 = imagen_lista.resize((25, 25), Image.LANCZOS)  # Ajusta el tamaño según sea necesario
        self.icono_lista = ImageTk.PhotoImage(imagen_redimensionada2)

    def crear_botones(self): #metodo para crear los botones de la ventana principal
        self.btn_celular = Button(self.frame_botones, text="Celular", command=lambda: self.mostrar_menu_bajo_boton(self.btn_celular, self.menu_celular))
        self.btn_celular.grid(row=0, column=0, sticky="w")

        self.btn_computador = Button(self.frame_botones, text="Computador", command=lambda: self.mostrar_menu_bajo_boton(self.btn_computador, self.menu_computador))
        self.btn_computador.grid(row=0, column=1, sticky="w")

        # Label para mostrar la imagen a la izquierda del botón
        self.lbl_icono = Label(self.root, image=self.icono_calculadora, bg="#E3F2FD")
        self.lbl_icono.place(relx=0.42, rely=0.5, anchor="center")  # Ajusta la posición según sea necesario

        # Label para mostrar la imagen a la izquierda del botón
        self.lbl_icono = Label(self.root, image=self.icono_lista, bg="#E3F2FD")
        self.lbl_icono.place(relx=0.42, rely=0.4, anchor="center")  # Ajusta la posición según sea necesario

        boton_ancho = 15
        self.btn_listar = Button(self.root, text="Listar", width=boton_ancho, command=self.abrir_ventana_listar)
        self.btn_listar.place(relx=0.5, rely=0.4, anchor="center")
        
        self.btn_calcular = Button(self.root, text="Calcular Precio", width=boton_ancho ,command=self.abrir_ventana_precio)
        self.btn_calcular.place(relx=0.5, rely=0.5, anchor="center")

        self.btn_acerca = Button(self.frame_botones, text="Acerca de", command=self.abrir_ventana_acerca)
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
        
    def abrir_ventana_buscar_celular(self): #metodo para abrir la ventana de buscar celular
        VentanaBuscarCelular(self.root, self.servidor)
    
    def abrir_ventana_buscar_computador(self): #metodo para abrir la ventana de buscar computador
        VentanaBuscarComputador(self.root, self.servidor)
    
    def abrir_ventana_eliminar_celular(self): #metodo para abrir la ventana de eliminar celular
        VentanaEliminarCelular(self.root, self.servidor)
        
    def abrir_ventana_eliminar_computador(self): #metodo para abrir la ventana de eliminar computador
        VentanaEliminarComputador(self.root, self.servidor)
    
    def generar_datos_prueba(self): #metodo para generar datos de prueba para la tienda
        self.servidor.agregar_computador("Dell XPS 13", "Computadora ultradelgada", 1199, 20, "Dell", "Intel Iris Xe", 16)
        self.servidor.agregar_computador("MacBook Pro 14", "Computadora de alto rendimiento", 1999, 15, "Apple", "Apple M1 Pro", 16)
        self.servidor.agregar_computador("HP Spectre x360", "Computadora convertible", 1399, 25, "HP", "Intel Iris Xe", 16)
        self.servidor.agregar_computador("Lenovo ThinkPad X1", "Computadora para profesionales", 1499, 18, "Lenovo", "Intel UHD", 32)
        self.servidor.agregar_computador("Asus ZenBook 14", "Computadora ultradelgada con gran batería", 1099, 30, "Asus", "NVIDIA GeForce MX450", 8)
        self.servidor.agregar_computador("Acer Swift 3", "Computadora ligera para productividad", 799, 40, "Acer", "AMD Radeon", 8)
        self.servidor.agregar_computador("Microsoft Surface Laptop 4", "Computadora con pantalla táctil", 1299, 22, "Microsoft", "Intel Iris Xe", 16)
        self.servidor.agregar_computador("Razer Blade 15", "Computadora gamer con gran rendimiento", 2199, 10, "Razer", "NVIDIA GeForce RTX 3070",16)
        self.servidor.agregar_computador("Samsung Galaxy Book Pro 360", "Computadora convertible con pantalla AMOLED", 1399, 17, "Samsung", "Intel Iris Xe", 16)
        self.servidor.agregar_computador("Gigabyte Aorus 15G", "Computadora gamer con teclado mecánico", 1699, 12, "Gigabyte", "NVIDIA GeForce RTX 3060", 16)
        self.servidor.agregar_celular("Samsung Galaxy S22", "Smartphone de gama alta", 799, 50, "Samsung", 128, "2022-02-25")
        self.servidor.agregar_celular("iPhone 13", "Smartphone con cámara avanzada", 899, 40, "Apple", 256, "2021-09-14")
        self.servidor.agregar_celular("Xiaomi Mi 11", "Smartphone de gran rendimiento", 749, 60, "Xiaomi", 128, "2021-01-01")
        self.servidor.agregar_celular("Huawei P50", "Smartphone con cámara Leica", 899, 45, "Huawei", 256, "2021-07-29")
        self.servidor.agregar_celular("OnePlus 9", "Smartphone con carga rápida", 729, 55, "OnePlus", 128, "2021-03-23")
        self.servidor.agregar_celular("Google Pixel 6", "Smartphone con Android puro", 799, 50, "Google", 128, "2021-10-28")
        self.servidor.agregar_celular("Oppo Find X3", "Smartphone con cámara 4K", 849, 40, "Oppo", 256, "2021-03-11")
        self.servidor.agregar_celular("Sony Xperia 5 II", "Smartphone con pantalla 120Hz", 949, 35, "Sony", 128, "2020-09-29")
        self.servidor.agregar_celular("Motorola Edge+", "Smartphone con pantalla OLED", 999, 30, "Motorola", 256, "2020-04-22")
        self.servidor.agregar_celular("Asus ROG Phone 5", "Smartphone gamer con gran batería", 1099, 25, "Asus", 512, "2021-03-10")
       
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