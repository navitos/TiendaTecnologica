from tkinter import Toplevel, Label

class VentanaAcerca:
    def __init__(self, root):
        self.ventana = Toplevel(root)
        self.ventana.title("Menú acerca de")
        self.ventana.minsize(width=300, height=200)
        self.centrar_ventana(self.ventana)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        Label(self.ventana, text="David Alejandro Gutiérrez Hernández - 2220211001").pack(pady=5)
        Label(self.ventana, text="Julián Rubiano Santofimio - 2220211015").pack(pady=5)
        Label(self.ventana, text="David Alejandro De Los Reyes Ostos - 2220221059").pack(pady=5)
        Label(self.ventana, text="Jose Ariel Reséndiz Perez").pack(pady=5)