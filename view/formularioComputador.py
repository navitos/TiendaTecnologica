from tkinter import *
from tkinter import messagebox

class FormularioComputador:
    def __init__(self, root, servicio):

        self.servicio = servicio
        self.nueva_ventana = Toplevel(root)
        self.nueva_ventana.title("Añadir Computador")
        self.nueva_ventana.minsize(width=300, height=350)
        
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
        
        Label(self.nueva_ventana, text="grafica:").pack()
        self.entry_grafica = Entry(self.nueva_ventana)
        self.entry_grafica.pack()
        
        Label(self.nueva_ventana, text="RAM:").pack()
        self.entry_ram = Entry(self.nueva_ventana)
        self.entry_ram.pack()
        
        # Botón para guardar
        Button(self.nueva_ventana, text="Guardar", command=self.guardar_computador).pack(pady=10)

    def guardar_computador(self):
        try:
            # Obtener los valores de los campos de entrada
            nombre = self.entry_nombre.get()
            descripcion = self.entry_descripcion.get()
            precio = float(self.entry_precio.get())
            stock = int(self.entry_stock.get())
            marca = self.entry_marca.get()
            grafica = self.entry_grafica.get()
            ram = float(self.entry_ram.get())

            # Llamar al método agregar_computador del controlador de tienda
            self.servicio.agregar_computador(nombre, descripcion, precio, stock, marca, grafica, ram)
            self.servicio.get_producto(-1)
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Computador agregado correctamente")
            
            # Cerrar la ventana después de guardar
            self.nueva_ventana.destroy()
        
        except ValueError as e:
            # Mostrar mensaje de error si hay un problema con los datos ingresados
            messagebox.showerror("Error", str(e))