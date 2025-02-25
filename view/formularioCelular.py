from tkinter import *

class FormularioCelular:
    def __init__(self, root):
        self.nueva_ventana = Toplevel(root)
        self.nueva_ventana.title("Añadir Celular")
        self.nueva_ventana.minsize(width=300, height=350)
        
        Label(self.nueva_ventana, text="Nombre:").pack()
        Entry(self.nueva_ventana).pack()
        Label(self.nueva_ventana, text="Stock:").pack()
        Entry(self.nueva_ventana).pack()
        Label(self.nueva_ventana, text="Precio:").pack()
        Entry(self.nueva_ventana).pack()
        Label(self.nueva_ventana, text="Marca:").pack()
        Entry(self.nueva_ventana).pack()
        Label(self.nueva_ventana, text="Tamaño:").pack()
        Entry(self.nueva_ventana).pack()
        Label(self.nueva_ventana, text="Fecha de lanzamiento:").pack()
        Entry(self.nueva_ventana).pack()
        
        Button(self.nueva_ventana, text="Guardar").pack(pady=10)