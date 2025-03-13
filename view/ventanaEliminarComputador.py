from tkinter import Toplevel, Label, Entry, Button, messagebox

from model.computador import Computador

class VentanaEliminarComputador:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Eliminar Computador")
        self.ventana.minsize(width=400, height=150)
        self.ventana.resizable(False, False)  # Hacerla no redimensionable
        self.centrar_ventana(self.ventana)  # Centrar la ventana

        # Campo de entrada para el nombre del celular
        Label(self.ventana, text="Nombre del computador:", font=("Arial", 10)).pack(pady=10)
        self.entry_nombre = Entry(self.ventana, font=("Arial", 10))
        self.entry_nombre.pack(pady=5)

        # Botón para eliminar
        Button(self.ventana, text="Eliminar", font=("Arial", 10), command=self.eliminar_celular).pack(pady=10)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def eliminar_celular(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del computador

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del computador.")
            return

        # Buscar el computador en la lista
        computador = self.controlador_tienda.buscar_producto(nombre)

        if computador and isinstance(computador, Computador):  # Verificar si es un computador
            # Eliminar el celular
            self.controlador_tienda.eliminar_producto(computador)
            messagebox.showinfo("Éxito", f"El celular '{nombre}' ha sido eliminado.")
            self.ventana.destroy()  # Cerrar la ventana después de eliminar
        else:
            messagebox.showinfo("Información", f"No se encontró un celular con el nombre '{nombre}'.")