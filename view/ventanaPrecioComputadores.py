from tkinter import Toplevel, Label
from tkinter import messagebox

class VentanaPrecioComputadores:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Precio Total de Computadores")
        self.ventana.minsize(width=350, height=100)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Calcular el precio total de los computadores
        precio_total = self.controlador_tienda.calcular_total_computadores()

        # Mostrar el precio total en la ventana
        Label(self.ventana, text=f"Precio total de los computadores: ${precio_total:.2f}", font=("Arial", 10)).pack(pady=20)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")