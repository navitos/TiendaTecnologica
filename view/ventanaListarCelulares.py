from tkinter import Toplevel, Frame, Button, BOTH, LEFT, RIGHT, Y, X, END
from tkinter import ttk
from services.observable import Observable
from services.controladorTienda import ControladorTienda

from model.celular import Celular

class VentanaListarCelulares:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        self.controlador_tienda.observable.agregar_observador(self)

        self.ventana = Toplevel(self.root)
        self.ventana.title("Listar Celulares")
        self.ventana.minsize(width=900, height=300)
        self.ventana.resizable(False, False)  # Hacerla no redimensionable
        self.centrar_ventana(self.ventana)  # Centrar la ventana

        # Crear un frame para contener la tabla y las barras de desplazamiento
        self.frame_tabla = Frame(self.ventana)
        self.frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Crear un Treeview para mostrar la tabla
        columnas = ("Nombre", "Descripción", "Precio", "Stock", "Marca", "Capacidad", "Fecha Lanzamiento")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        # Configurar las columnas
        anchos_columnas = [150, 200, 80, 50, 100, 80, 80]
        for col, ancho in zip(columnas, anchos_columnas):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor="center")

        # Agregar barras de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tabla.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

        # Botones de paginación
        self.frame_paginacion = Frame(self.ventana)
        self.frame_paginacion.pack(pady=10)

        self.pagina_actual = 1
        self.elementos_por_pagina = 15  # Mostrar 5 elementos por página

        self.btn_anterior = Button(self.frame_paginacion, text="Anterior", command=self.pagina_anterior)
        self.btn_anterior.pack(side=LEFT, padx=5)

        self.btn_siguiente = Button(self.frame_paginacion, text="Siguiente", command=self.pagina_siguiente)
        self.btn_siguiente.pack(side=LEFT, padx=5)

        # Mostrar la primera página
        self.mostrar_pagina()

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def mostrar_pagina(self):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener los computadores de la página actual
        inicio = (self.pagina_actual - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        celulares_pagina = self.controlador_tienda.productos[inicio:fin]

        # Agregar los computadores a la tabla
        for producto in celulares_pagina:
            if isinstance(producto, Celular): 
                self.tabla.insert("", END, values=(
                    producto.get_nombre(),
                    producto.get_descripcion(),
                    f"${producto.get_precio():.2f}",
                    producto.get_stock(),
                    producto.get_marca(),
                    producto.get_capacidad(),
                    f"{producto.get_fechaLanzamiento} ",
                ))

    def pagina_anterior(self):
        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.mostrar_pagina()

    def pagina_siguiente(self):
        total_paginas = (len(self.controlador_tienda.productos) // self.elementos_por_pagina) + 1
        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.mostrar_pagina()

    def actualizar(self, mensaje):
        print("notificacion")
        self.mostrar_pagina()