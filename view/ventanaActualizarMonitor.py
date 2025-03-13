# En view/ventanaActualizarMonitor.py
from tkinter import Toplevel, Label, Entry, Button, messagebox
from model.monitor import Monitor

class VentanaActualizarMonitor:
    def __init__(self, root, controlador_tienda, computador, callback_actualizacion):
        self.root = root
        self.controlador_tienda = controlador_tienda
        self.computador = computador
        self.callback_actualizacion = callback_actualizacion

        self.ventana = Toplevel(self.root)
        self.ventana.title("Actualizar Monitor")
        self.ventana.minsize(width=300, height=250)
        self.centrar_ventana(self.ventana)
        self.ventana.resizable(False, False)

        # Obtener el monitor actual del computador
        self.monitor = self.computador.get_monitor()

        # Campos de entrada
        Label(self.ventana, text="Marca del monitor:").pack(pady=5)
        self.entry_descripcion = Entry(self.ventana)
        self.entry_descripcion.insert(0, self.monitor.get_marca())
        self.entry_descripcion.pack(pady=5)

        Label(self.ventana, text="Tamaño (pulgadas):").pack(pady=5)
        self.entry_tamano = Entry(self.ventana)
        self.entry_tamano.insert(0, str(self.monitor.get_tamanio()))
        self.entry_tamano.pack(pady=5)

        Label(self.ventana, text="Frecuencia (Hz):").pack(pady=5)
        self.entry_frecuencia = Entry(self.ventana)
        self.entry_frecuencia.insert(0, str(self.monitor.get_frecuencia()))
        self.entry_frecuencia.pack(pady=5)

        # Botón de actualización
        Button(self.ventana, text="Actualizar Monitor", command=self.actualizar_monitor).pack(pady=10)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def actualizar_monitor(self):
        try:
            nueva_descripcion = self.entry_descripcion.get()
            nuevo_tamano = float(self.entry_tamano.get())
            nueva_frecuencia = int(self.entry_frecuencia.get())

            if nuevo_tamano <= 0 or nueva_frecuencia <= 0:
                raise ValueError("Los valores deben ser positivos")

            # Actualizar el monitor
            self.monitor.set_marca(nueva_descripcion)
            self.monitor.set_tamanio(nuevo_tamano)
            self.monitor.set_frecuencia(nueva_frecuencia)

            
            self.callback_actualizacion()  # Actualizar la vista principal

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")