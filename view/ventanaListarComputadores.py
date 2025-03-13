from tkinter import Toplevel, Frame, Button, BOTH, LEFT, RIGHT, Y, X, END
from tkinter import ttk

from model.computador import Computador

class VentanaListarComputadores:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        self.ventana = Toplevel(self.root)
        self.ventana.title("Listar Computadores")
        self.ventana.minsize(width=850, height=300)
        self.centrar_ventana(self.ventana)  # Centrar la ventana
        self.ventana.resizable(False, False)  # Hacerla no redimensionable

        # Crear un frame para contener la tabla y las barras de desplazamiento
        self.frame_tabla = Frame(self.ventana)
        self.frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Crear un Treeview para mostrar la tabla
        columnas = ("Nombre", "Descripción", "Precio", "Stock", "Marca", "Gráfica", "RAM", "Monitor")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        # Configurar las columnas
        anchos_columnas = [150, 200, 80, 50, 100, 80, 50,100]
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
        self.controlador_tienda.observable.agregar_observador(self)

        # Mostrar la primera página
        self.mostrar_pagina()

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar la geometría de la ventana
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def obtener_computadores(self):
        # Filtrar solo los computadores de la lista de productos
        return [producto for producto in self.controlador_tienda.productos if isinstance(producto, Computador)]

    def mostrar_pagina(self):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener los computadores de la página actual
        computadores = self.obtener_computadores()
        inicio = (self.pagina_actual - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        computadores_pagina = computadores[inicio:fin]

        # Agregar los computadores a la tabla
        for computador in computadores_pagina:
            self.tabla.insert("", END, values=(
                computador.get_nombre(),
                computador.get_descripcion(),
                f"${computador.get_precio():.2f}",
                computador.get_stock(),
                computador.get_marca(),
                computador.get_grafica(),
                f"{computador.get_ram()} GB",
                f"{computador.get_monitor().get_frecuencia()} Hz"
                
            ))

    def pagina_anterior(self):
        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.mostrar_pagina()

    def pagina_siguiente(self):
        computadores = self.obtener_computadores()
        total_paginas = (len(computadores) // self.elementos_por_pagina) + 1
        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.mostrar_pagina()

    def actualizar(self, mensaje):
        print("notificacion")
        self.mostrar_pagina()