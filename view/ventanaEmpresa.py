import ttkbootstrap as ttk
import tkinter as tk

class VentanaEmpresa(tk.Toplevel):
    def __init__(self, parent, empresa_singleton):
        super().__init__(parent)
        self.title("Información de la Empresa (Singleton)")

        # Recibimos la instancia única de la empresa
        self.empresa = empresa_singleton

        # Etiquetas con la información
        ttk.Label(self, text=f"NIT: {self.empresa.nit}").pack(pady=5)
        ttk.Label(self, text=f"Nombre: {self.empresa.nombre}").pack(pady=5)
        ttk.Label(self, text=f"Razón Social: {self.empresa.razon_social}").pack(pady=5)

        # Llamada para centrar y definir el tamaño de la ventana
        self.centrar_ventana()

    def centrar_ventana(self):
        """
        Ajusta la posición y tamaño inicial para que aparezca centrada en la pantalla.
        """
        # Asegura que tkinter calcule el layout antes de posicionar
        self.update_idletasks()

        # Aumenta el tamaño para que se aprecie el título en la barra
        ancho_ventana = 400
        alto_ventana = 200

        # Calcula coordenadas para centrar en la pantalla
        x = (self.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (self.winfo_screenheight() // 2) - (alto_ventana // 2)

        # Aplica la geometría resultante (dimensiones + posición)
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")