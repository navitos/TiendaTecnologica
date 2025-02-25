from model.computador import Computador
from tkinter import Toplevel, Label, Entry, Button, messagebox

class VentanaBuscarComputador:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Buscar Computador")
        self.ventana.minsize(width=400, height=400)
        self.ventana.resizable(False, False)  # Hacerla no redimensionable
        self.centrar_ventana(self.ventana)  # Centrar la ventana

        # Campo de entrada para el nombre del celular
        Label(self.ventana, text="Nombre del computador:", font=("Arial", 10)).pack(pady=10)
        self.entry_nombre = Entry(self.ventana, font=("Arial", 10))
        self.entry_nombre.pack(pady=5)

        # Botón para buscar
        Button(self.ventana, text="Buscar", font=("Arial", 10), command=self.buscar_computador).pack(pady=10)

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

    def buscar_computador(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del celular

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del computador.")
            return

        # Buscar el celular en la lista
        computador = self.controlador_tienda.buscar_producto(nombre)

        if computador and isinstance(computador, Computador):  # Verificar si es un celular
            # Mostrar los atributos del celular
            atributos = (
                f"Nombre: {computador.get_nombre()}\n"
                f"Descripción: {computador.get_descripcion()}\n"
                f"Precio: ${computador.get_precio():.2f}\n"
                f"Stock: {computador.get_stock()}\n"
                f"Marca: {computador.get_marca()}\n"
                f"Tarjeta gráfica: {computador.get_grafica()}\n"
                f"RAM: {computador.get_ram()} GB"
                
            )
            self.label_resultado.config(text=atributos)
        else:
            messagebox.showinfo("Información", f"No se encontró un computador con el nombre '{nombre}'.")
            self.label_resultado.config(text="")