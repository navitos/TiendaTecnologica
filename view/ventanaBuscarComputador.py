from model.computador import Computador
from tkinter import END, Frame, Toplevel, Label, Entry, Button, messagebox

from view.ventanaActualizarMonitor import VentanaActualizarMonitor

class VentanaBuscarComputador:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        # Crear la ventana emergente
        self.ventana = Toplevel(self.root)
        self.ventana.title("Consultar Computador")
        self.ventana.minsize(width=400, height=600)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Campo de entrada para el nombre del computador
        Label(self.ventana, text="Nombre del computador:", font=("Arial", 12)).pack(pady=10)
        self.entry_nombre = Entry(self.ventana, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)

        # Botón para buscar
        Button(self.ventana, text="Buscar", font=("Arial", 12), command=self.buscar_computador).pack(pady=10)
        Button(self.ventana, text="Eliminar", font=("Arial", 12), command=self.eliminar_computador).pack(pady=10)


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

        Label(self.frame_actualizar, text="Nueva gráfica:").grid(row=5, column=0, padx=5, pady=5)
        self.entry_nueva_grafica = Entry(self.frame_actualizar)
        self.entry_nueva_grafica.grid(row=5, column=1, padx=5, pady=5)

        Label(self.frame_actualizar, text="Nueva RAM:").grid(row=6, column=0, padx=5, pady=5)
        self.entry_nueva_ram = Entry(self.frame_actualizar)
        self.entry_nueva_ram.grid(row=6, column=1, padx=5, pady=5)

        # Botón para actualizar
        self.btn_actualizar = Button(self.ventana, text="Actualizar", font=("Arial", 12), command=self.actualizar_computador)
        self.btn_actualizar.pack(pady=10)
        self.btn_actualizar.config(state="disabled")  # Deshabilitar el botón inicialmente

        # Variable para almacenar el computador encontrado
        self.computador_encontrado = None
        
        # Botón para actualizar monitor
        self.btn_actualizar_monitor = Button(self.ventana, text="Actualizar Monitor", 
                                           font=("Arial", 12), command=self.abrir_ventana_actualizar_monitor)
        self.btn_actualizar_monitor.pack(pady=5)
        self.btn_actualizar_monitor.config(state="disabled")

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def buscar_computador(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del computador

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del computador.")
            return

        # Buscar el computador en la lista
        self.computador_encontrado = self.controlador_tienda.buscar_producto(nombre)

        if self.computador_encontrado and isinstance(self.computador_encontrado, Computador):  # Verificar si es un computador

            # Habilitar el botón de actualizar
            self.btn_actualizar.config(state="normal")

            # Llenar los campos de actualización con los valores actuales
            self.entry_nuevo_nombre.insert(0, self.computador_encontrado.get_nombre())
            self.entry_nueva_descripcion.insert(0, self.computador_encontrado.get_descripcion())
            self.entry_nuevo_precio.insert(0, str(self.computador_encontrado.get_precio()))
            self.entry_nuevo_stock.insert(0, str(self.computador_encontrado.get_stock()))
            self.entry_nueva_marca.insert(0, self.computador_encontrado.get_marca())
            self.entry_nueva_grafica.insert(0, self.computador_encontrado.get_grafica())
            self.entry_nueva_ram.insert(0, str(self.computador_encontrado.get_ram()))
            self.btn_actualizar_monitor.config(state="normal")  # Habilitar nuevo botón
        else:
            messagebox.showinfo("Información", f"No se encontró un computador con el nombre '{nombre}'.")
            self.btn_actualizar.config(state="disabled")  # Deshabilitar el botón si no se encuentra el computador

    def actualizar_computador(self):
        if not self.computador_encontrado:
            messagebox.showwarning("Advertencia", "No hay un computador seleccionado para actualizar.")
            return

        try:
            # Obtener los nuevos valores de los campos de entrada
            nuevo_nombre = self.entry_nuevo_nombre.get().strip()
            nueva_descripcion = self.entry_nueva_descripcion.get().strip()
            nuevo_precio = float(self.entry_nuevo_precio.get())
            nuevo_stock = int(self.entry_nuevo_stock.get())
            nueva_marca = self.entry_nueva_marca.get().strip()
            nueva_grafica = self.entry_nueva_grafica.get().strip()
            nueva_ram = int(self.entry_nueva_ram.get())

            # Actualizar los atributos del computador
            self.computador_encontrado.set_nombre(nuevo_nombre)
            self.computador_encontrado.set_descripcion(nueva_descripcion)
            self.computador_encontrado.set_precio(nuevo_precio)
            self.computador_encontrado.set_stock(nuevo_stock)
            self.computador_encontrado.set_marca(nueva_marca)
            self.computador_encontrado.set_grafica(nueva_grafica)
            self.computador_encontrado.set_ram(nueva_ram)

            self.controlador_tienda.observable.notificar_observadores_computador("notificacion")
            self.controlador_tienda.observable.notificar_observadores("notificacion")

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "El computador ha sido actualizado correctamente.")


        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

    def eliminar_computador(self):
        nombre = self.entry_nombre.get().strip()  # Obtener el nombre del computador

        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del computador.")
            return

        # Buscar el computador en la lista
        computador = self.controlador_tienda.buscar_producto(nombre)

        if computador and isinstance(computador, Computador):  # Verificar si es un computador
            # Eliminar el celular
            self.controlador_tienda.eliminar_producto(computador)

            self.controlador_tienda.observable.notificar_observadores_computador("notificacion")
            self.controlador_tienda.observable.notificar_observadores("notificacion")

            messagebox.showinfo("Éxito", f"El computador '{nombre}' ha sido eliminado.")

            self.limpiar_campos()
            
        else:
            messagebox.showinfo("Información", f"No se encontró un computador con el nombre '{nombre}'.")

    def limpiar_campos(self):
        # Limpiar los campos de entrada
        self.entry_nuevo_nombre.delete(0, END)
        self.entry_nueva_descripcion.delete(0, END)
        self.entry_nuevo_precio.delete(0, END)
        self.entry_nuevo_stock.delete(0, END)
        self.entry_nueva_marca.delete(0, END)
        self.entry_nueva_grafica.delete(0, END)
        self.entry_nueva_ram.delete(0, END)

        # Deshabilitar los botones de actualizar y eliminar
        self.btn_actualizar.config(state="disabled")

        # Reiniciar la variable del computador encontrado
        self.computador_encontrado = None
    
    def abrir_ventana_actualizar_monitor(self):
        VentanaActualizarMonitor(
            self.root,
            self.controlador_tienda,
            self.computador_encontrado,
            self.actualizar_vista
            
        )
        
    def actualizar_vista(self):  
        self.controlador_tienda.observable.notificar_observadores_computador("notificacion")
        self.controlador_tienda.observable.notificar_observadores("notificacion")
    