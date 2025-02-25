from tkinter import *
from tkinter import messagebox
from model.celular import Celular
from services.controladorTienda import ControladorTienda

class FormularioCelular:
    def __init__(self, root, servicio):
        self.servicio = servicio
        self.nueva_ventana = Toplevel(root)
        self.nueva_ventana.title("Añadir Celular")
        self.nueva_ventana.minsize(width=400, height=400)
        self.centrar_ventana(self.nueva_ventana)
        
        # Campos de entrada
        Label(self.nueva_ventana, text="Nombre:").pack()
        self.entry_nombre = Entry(self.nueva_ventana)
        self.entry_nombre.pack()
        
        Label(self.nueva_ventana, text="Descripción:").pack()
        self.entry_descripcion = Entry(self.nueva_ventana)
        self.entry_descripcion.pack()
        
        Label(self.nueva_ventana, text="Precio:").pack()
        self.entry_precio = Entry(self.nueva_ventana)
        self.entry_precio.pack()
        
        Label(self.nueva_ventana, text="Stock:").pack()
        self.entry_stock = Entry(self.nueva_ventana)
        self.entry_stock.pack()
        
        Label(self.nueva_ventana, text="Marca:").pack()
        self.entry_marca = Entry(self.nueva_ventana)
        self.entry_marca.pack()
        
        Label(self.nueva_ventana, text="Capacidad:").pack()
        self.entry_capacidad = Entry(self.nueva_ventana)
        self.entry_capacidad.pack()
        
        Label(self.nueva_ventana, text="Fecha de lanzamiento:").pack()
        self.entry_fechaLanzamiento = Entry(self.nueva_ventana)
        self.entry_fechaLanzamiento.pack()
        
        # Botón para guardar
        Button(self.nueva_ventana, text="Guardar", command=self.guardar_celular).pack(pady=10)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def guardar_celular(self):
        try:
            # Obtener los valores de los campos de entrada
            nombre = self.entry_nombre.get()
            descripcion = self.entry_descripcion.get()
            precio = float(self.entry_precio.get())
            stock = int(self.entry_stock.get())
            marca = self.entry_marca.get()
            capacidad = float(self.entry_capacidad.get())
            fechaLanzamiento = self.entry_fechaLanzamiento.get()

            # Llamar al método agregar_celular del controlador de tienda
            self.servicio.agregar_celular(nombre, descripcion, precio, stock, marca, capacidad, fechaLanzamiento)
            self.servicio.mostrar_productos()
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Celular agregado correctamente")
            
            # Cerrar la ventana después de guardar
            self.nueva_ventana.destroy()
        
        except ValueError as e:
            # Mostrar mensaje de error si hay un problema con los datos ingresados
            messagebox.showerror("Error", str(e))