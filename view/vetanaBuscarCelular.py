from tkinter import END, Frame, Toplevel, Label, Entry, Button, messagebox

from model.celular import Celular

class VentanaBuscarCelular:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Buscar Celular")
        self.ventana.minsize(width=400, height=500)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Campo de entrada para el nombre del celular
        Label(self.ventana, text="Nombre del celular:", font=("Arial", 12)).pack(pady=10)
        self.entry_nombre = Entry(self.ventana, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)

        # Botón para buscar
        Button(self.ventana, text="Buscar", font=("Arial", 12), command=self.buscar_celular).pack(pady=10)

        Button(self.ventana, text="Eliminar", font=("Arial", 10), command=self.eliminar_celular).pack(pady=10)


        # Campos de entrada para actualizar los atributos
        self.frame_actualizar = Frame(self.ventana)
        self.frame_actualizar.pack(pady=10)

        Label(self.frame_actualizar, text="Nuevo nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nuevo_nombre = Entry(self.frame_actualizar)
        self.entry_nuevo_nombre.grid(row=0, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nueva descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_nueva_descripcion = Entry(self.frame_actualizar)
        self.entry_nueva_descripcion.grid(row=1, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nuevo precio:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_nuevo_precio = Entry(self.frame_actualizar)
        self.entry_nuevo_precio.grid(row=2, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nuevo stock:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_nuevo_stock = Entry(self.frame_actualizar)
        self.entry_nuevo_stock.grid(row=3, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nueva marca:").grid(row=4, column=0, padx=5, pady=5)
        self.entry_nueva_marca = Entry(self.frame_actualizar)
        self.entry_nueva_marca.grid(row=4, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nueva capacidad:").grid(row=5, column=0, padx=5, pady=5)
        self.entry_nueva_capacidad = Entry(self.frame_actualizar)
        self.entry_nueva_capacidad.grid(row=5, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nueva fecha de lanzamiento:").grid(row=6, column=0, padx=5, pady=5)
        self.entry_nueva_fechaLanzamiento = Entry(self.frame_actualizar)
        self.entry_nueva_fechaLanzamiento.grid(row=6, column=1, padx=5, pady=5)

        # Botón para actualizar
        self.btn_actualizar = Button(self.ventana, text="Actualizar", font=("Arial", 12), command=self.actualizar_celular)
        self.btn_actualizar.pack(pady=10)
        self.btn_actualizar.config(state="disabled")  # Deshabilitar el botón inicialmente

        # Variable para almacenar el celular encontrado
        self.celular_encontrado = None

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
        self.celular_encontrado = self.controlador_tienda.buscar_producto(nombre)

        if self.celular_encontrado and isinstance(self.celular_encontrado, Celular):  # Verificar si es un celular

            # Habilitar el botón de actualizar
            self.btn_actualizar.config(state="normal")

            # Llenar los campos de actualización con los valores actuales
            self.entry_nuevo_nombre.insert(0, self.celular_encontrado.get_nombre())
            self.entry_nueva_descripcion.insert(0, self.celular_encontrado.get_descripcion())
            self.entry_nuevo_precio.insert(0, str(self.celular_encontrado.get_precio()))
            self.entry_nuevo_stock.insert(0, str(self.celular_encontrado.get_stock()))
            self.entry_nueva_marca.insert(0, self.celular_encontrado.get_marca())
            self.entry_nueva_capacidad.insert(0, str(self.celular_encontrado.get_capacidad()))
            self.entry_nueva_fechaLanzamiento.insert(0, self.celular_encontrado.get_fechaLanzamiento())
        else:
            messagebox.showinfo("Información", f"No se encontró un celular con el nombre '{nombre}'.")
            self.btn_actualizar.config(state="disabled")  # Deshabilitar el botón si no se encuentra el celular

    def actualizar_celular(self):
        if not self.celular_encontrado:
            messagebox.showwarning("Advertencia", "No hay un celular seleccionado para actualizar.")
            return

        try:
            # Obtener los nuevos valores de los campos de entrada
            nuevo_nombre = self.entry_nuevo_nombre.get().strip()
            nueva_descripcion = self.entry_nueva_descripcion.get().strip()
            nuevo_precio = float(self.entry_nuevo_precio.get())
            nuevo_stock = int(self.entry_nuevo_stock.get())
            nueva_marca = self.entry_nueva_marca.get().strip()
            nueva_capacidad = float(self.entry_nueva_capacidad.get())
            nueva_fechaLanzamiento = self.entry_nueva_fechaLanzamiento.get().strip()

            # Actualizar los atributos del celular
            self.celular_encontrado.set_nombre(nuevo_nombre)
            self.celular_encontrado.set_descripcion(nueva_descripcion)
            self.celular_encontrado.set_precio(nuevo_precio)
            self.celular_encontrado.set_stock(nuevo_stock)
            self.celular_encontrado.set_marca(nueva_marca)
            self.celular_encontrado.set_capacidad(nueva_capacidad)
            self.celular_encontrado.set_fechaLanzamiento(nueva_fechaLanzamiento)

            # Mostrar mensaje de éxito
            self.controlador_tienda.observable.notificar_observadores_celular("notificacion")
            self.controlador_tienda.observable.notificar_observadores("notificacion")
            messagebox.showinfo("Éxito", "El celular ha sido actualizado correctamente.")

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
        

    def eliminar_celular(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del celular

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del celular.")
            return

        # Buscar el celular en la lista
        celular = self.controlador_tienda.buscar_producto(nombre)

        if celular and isinstance(celular, Celular):  # Verificar si es un celular
            # Eliminar el celular
            self.controlador_tienda.eliminar_producto(celular)
            self.controlador_tienda.observable.notificar_observadores_celular("notificacion")
            self.controlador_tienda.observable.notificar_observadores("notificacion")


            messagebox.showinfo("Éxito", f"El celular '{nombre}' ha sido eliminado.")

            self.limpiar_campos()
            
        else:
            messagebox.showinfo("Información", f"No se encontró un celular con el nombre '{nombre}'.")

    def limpiar_campos(self):
        # Limpiar los campos de entrada
        self.entry_nuevo_nombre.delete(0, END)
        self.entry_nueva_descripcion.delete(0, END)
        self.entry_nuevo_precio.delete(0, END)
        self.entry_nuevo_stock.delete(0, END)
        self.entry_nueva_marca.delete(0, END)
        self.entry_nueva_fechaLanzamiento.delete(0, END)
        self.entry_nueva_capacidad.delete(0, END)

        # Deshabilitar los botones de actualizar y eliminar
        self.btn_actualizar.config(state="disabled")

        # Reiniciar la variable del computador encontrado
        self.celular_encontrado = None