import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from view.formularioCelular import FormularioCelular
from view.formularioComputador import FormularioComputador
from view.ventanaListar import VentanaListar
from view.ventanaAcerca import VentanaAcerca
from view.ventanaListarComputadores import VentanaListarComputadores
from view.ventanaPrecioComputadores import VentanaPrecioComputadores
from view.ventanaPrecioCelulares import VentanaPrecioCelulares
from services.controladorTienda import ControladorTienda
from view.ventanaPrecio import VentanaPrecio
from view.vetanaBuscarCelular import VentanaBuscarCelular
from view.ventanaBuscarComputador import VentanaBuscarComputador
from view.ventanaEliminarCelular import VentanaEliminarCelular
from view.ventanaEliminarComputador import VentanaEliminarComputador
#from tkinter import ttk
from PIL import Image, ImageTk

class TiendaApp:
    def __init__(self, root):
        self.menu_visible = True
        self.root = root
        self.root.title("Tienda Tecnológica")
        self.root.geometry("1000x600")  
        self.root.resizable(True, True)
        
        self.root.style = ttk.Style()  
        self.root.style.theme_use("cosmo")

        self.servidor = ControladorTienda([])
        self.crear_menu()
        
        self.crear_menu_lateral()
        self.generar_datos_prueba()
        self.agregar_imagen_centrada()
        self.centrar_ventana()
        


    def crear_menu(self):
        menubar = ttk.Menu(self.root)

        # Menú Celulares
        menu_celular = ttk.Menu(menubar, tearoff=0)
        menu_celular.add_command(label="Añadir Celular", command=self.abrir_ventana_celular)
        menu_celular.add_command(label="Consultar Celular", command=self.abrir_ventana_buscar_celular)
        menu_celular.add_command(label="Eliminar Celular", command=self.abrir_ventana_eliminar_celular)
        menu_celular.add_command(label="Calcular Precio", command=self.abrir_ventana_precio_celulares)
        menubar.add_cascade(label="📱 Celulares", menu=menu_celular)

        # Menú Computadores
        menu_computador = ttk.Menu(menubar, tearoff=0)
        menu_computador.add_command(label="Añadir Computador", command=self.abrir_ventana_computador)
        menu_computador.add_command(label="Consultar Computador", command=self.abrir_ventana_buscar_computador)
        menu_computador.add_command(label="Eliminar Computador", command=self.abrir_ventana_eliminar_computador)
        menu_computador.add_command(label="Calcular Precio", command=self.abrir_ventana_precio_computadores)
        menu_computador.add_command(label="Listar Computadores", command=self.abrir_ventana_listar_computadores)
        menubar.add_cascade(label="💻 Computadores", menu=menu_computador)

        # Menú Otras Opciones
        menu_otras = ttk.Menu(menubar, tearoff=0)
        menu_otras.add_separator()
        menu_otras.add_command(label="ℹ Acerca de", command=self.abrir_ventana_acerca)
        menubar.add_cascade(label="🔧 Más Opciones", menu=menu_otras)

        self.root.config(menu=menubar)

    def crear_menu_lateral(self):
        #"""Crea un menú lateral con los botones ubicados más abajo"""
        self.frame_menu = ttk.Frame(self.root, padding=10, width=200)
        self.frame_menu.pack(side=LEFT, fill=Y)

        # Frame interno para agrupar los botones y bajarlos
        self.frame_botones = ttk.Frame(self.frame_menu)
        self.frame_botones.pack(side=TOP, pady=50)  # Ajusta `pady` para mover más abajo

        ttk.Button(self.frame_botones, text="📜 Listar Productos", command=self.abrir_ventana_listar).pack(fill=X, pady=5)
        ttk.Button(self.frame_botones, text="💰 Calcular Precio", command=self.abrir_ventana_precio).pack(fill=X, pady=5)
        ttk.Button(self.frame_botones, text="ℹ Acerca de", command=self.abrir_ventana_acerca).pack(fill=X, pady=5)
        
        # Botón Toggle
        self.btn_toggle_menu = ttk.Button(self.root, text="☰", command=self.toggle_menu)
        self.btn_toggle_menu.place(x=10, y=10)
        #"""Dibuja una línea vertical para separar el menú de la imagen central"""
        self.separador = ttk.Separator(self.root, orient="vertical")
        self.separador.place(x=180, y=0, relheight=1)  # Línea vertical a la derecha del menú
    
    def toggle_menu(self):
        #"""Muestra u oculta el menú lateral"""
        if self.menu_visible:
            self.frame_menu.pack_forget()
        else:
            self.frame_menu.pack(side=LEFT, fill=Y)
        self.menu_visible = not self.menu_visible
        

    def agregar_imagen_centrada(self):
        #Carga y muestra una imagen PNG en el centro de la ventana principal
        try:
            # Cargar la imagen
            imagen_original = Image.open("view/resources/logo.png")  # Cambia esto a la ruta de tu imagen
            imagen_resized = imagen_original.resize((600, 600), Image.Resampling.LANCZOS)  # Ajusta el tamaño si es necesario
            
            # Convertir para Tkinter
            self.imagen_tk = ImageTk.PhotoImage(imagen_resized)

            # Crear Label con la imagen
            self.label_imagen = ttk.Label(self.root, image=self.imagen_tk)
            self.label_imagen.place(relx=0.6, rely=0.5, anchor="center")  # Centrar en la ventana
            print("Imagen Cargada")

        except Exception as e:
            print("Error al cargar la imagen:", e)

    def abrir_ventana_acerca(self):
        VentanaAcerca(self.root)

    def abrir_ventana_precio(self):
        VentanaPrecio(self.root, self.servidor)

    def abrir_ventana_celular(self):
        FormularioCelular(self.root, self.servidor)

    def abrir_ventana_computador(self):
        FormularioComputador(self.root, self.servidor)

    def abrir_ventana_listar(self):
        VentanaListar(self.root, self.servidor)

    def abrir_ventana_precio_computadores(self):
        VentanaPrecioComputadores(self.root, self.servidor)

    def abrir_ventana_precio_celulares(self):
        VentanaPrecioCelulares(self.root, self.servidor)

    def abrir_ventana_buscar_celular(self):
        VentanaBuscarCelular(self.root, self.servidor)

    def abrir_ventana_buscar_computador(self):
        VentanaBuscarComputador(self.root, self.servidor)

    def abrir_ventana_eliminar_celular(self):
        VentanaEliminarCelular(self.root, self.servidor)

    def abrir_ventana_eliminar_computador(self):
        VentanaEliminarComputador(self.root, self.servidor)

    def abrir_ventana_listar_computadores(self):
        VentanaListarComputadores(self.root, self.servidor)
    
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
        print("Productos agregados correctamente.")

    def centrar_ventana(self):
        #"""Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        ancho = 1000
        alto = 600
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

if __name__ == "__main__":
    
    root = ttk.Window(themename="superhero")  # Cambia el tema según prefieras
    app = TiendaApp(root)
    root.mainloop()
