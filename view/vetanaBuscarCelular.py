from tkinter import Toplevel, Label, Entry, Button, messagebox

from model.celular import Celular

class VentanaBuscarCelular:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Buscar Celular")
        self.ventana.minsize(width=400, height=400)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Campo de entrada para el nombre del celular
        Label(self.ventana, text="Nombre del celular:", font=("Arial", 12)).pack(pady=10)
        self.entry_nombre = Entry(self.ventana, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)

        # Botón para buscar
        Button(self.ventana, text="Buscar", font=("Arial", 10), command=self.buscar_celular).pack(pady=10)

        # Etiqueta para mostrar los atributos del celular
        self.label_resultado = Label(self.ventana, text="", font=("Arial", 10))
        self.label_resultado.pack(pady=10)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def buscar_celular(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del celular

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del celular.")
            return

        # Buscar el celular en la lista
        celular = self.controlador_tienda.buscar_producto(nombre)

        if celular and isinstance(celular, Celular):  # Verificar si es un celular
            # Mostrar los atributos del celular
            atributos = (
                f"Nombre: {celular.get_nombre()}\n"
                f"Descripción: {celular.get_descripcion()}\n"
                f"Precio: ${celular.get_precio():.2f}\n"
                f"Stock: {celular.get_stock()}\n"
                f"Marca: {celular.get_marca()}\n"
                f"Capacidad: {celular.get_capacidad()} GB\n"
                f"Fecha de lanzamiento: {celular.get_fechaLanzamiento()}"
            )
            self.label_resultado.config(text=atributos)
        else:
            messagebox.showinfo("Información", f"No se encontró un celular con el nombre '{nombre}'.")
            self.label_resultado.config(text="")