from tkinter import Toplevel, Frame, Button, BOTH, LEFT, RIGHT, Y, X, END
from tkinter import ttk

from model.celular import Celular

class VentanaListarCelulares:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        self.ventana = Toplevel(self.root)
        self.ventana.title("Listar Celulares")
        self.ventana.minsize(width=800, height=300)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Crear un frame para contener la tabla y las barras de desplazamiento
        self.frame_tabla = Frame(self.ventana)
        self.frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Crear un Treeview para mostrar la tabla
        columnas = ("Nombre", "Descripción", "Precio", "Stock", "Marca", "Capacidad", "Fecha Lanzamiento")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        # Configurar las columnas
        anchos_columnas = [150, 200, 80, 50, 100, 80, 120]
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
        self.elementos_por_pagina = 10  # Mostrar 5 elementos por página

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

    def obtener_celulares(self):
        # Filtrar solo los celulares de la lista de productos
        return [producto for producto in self.controlador_tienda.productos if isinstance(producto, Celular)]

    def mostrar_pagina(self):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener los celulares de la página actual
        celulares = self.obtener_celulares()
        inicio = (self.pagina_actual - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        celulares_pagina = celulares[inicio:fin]

        # Agregar los celulares a la tabla
        for celular in celulares_pagina:
            self.tabla.insert("", END, values=(
                celular.get_nombre(),
                celular.get_descripcion(),
                f"${celular.get_precio():.2f}",
                celular.get_stock(),
                celular.get_marca(),
                f"{celular.get_capacidad()} GB",
                celular.get_fechaLanzamiento()
            ))

    def pagina_anterior(self):
        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.mostrar_pagina()

    def pagina_siguiente(self):
        celulares = self.obtener_celulares()
        total_paginas = (len(celulares) // self.elementos_por_pagina) + 1
        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.mostrar_pagina()