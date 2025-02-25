from tkinter import Toplevel, Frame, Button, BOTH, LEFT, RIGHT, Y, X, END
from tkinter import ttk

class VentanaListar:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        self.ventana = Toplevel(self.root)
        self.ventana.title("Listar Productos")
        self.ventana.minsize(width=800, height=400)  # Aumentar el tamaño de la ventana
        
        self.ventana.resizable(False, False)  # Hacerla redimensionable
        self.centrar_ventana(self.ventana)  # Centrar la ventana

        # Crear un frame para contener la tabla y las barras de desplazamiento
        frame_tabla = Frame(self.ventana)
        frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)  # Margen interno

        # Crear un Treeview para mostrar la tabla
        columnas = ("Nombre", "Descripción", "Precio", "Stock", "Marca")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        # Configurar las columnas
        anchos_columnas = [150, 200, 80, 50, 100]  # Definir anchos personalizados
        for col, ancho in zip(columnas, anchos_columnas):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor="center")  # Centrar el contenido

        # Agregar barras de desplazamiento
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Botones de paginación
        frame_paginacion = Frame(self.ventana)
        frame_paginacion.pack(pady=10)

        self.pagina_actual = 1
        self.elementos_por_pagina = 15

        self.btn_anterior = Button(frame_paginacion, text="Anterior", command=self.pagina_anterior)
        self.btn_anterior.pack(side=LEFT, padx=5)

        self.btn_siguiente = Button(frame_paginacion, text="Siguiente", command=self.pagina_siguiente)
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

        # Obtener los productos de la página actual
        inicio = (self.pagina_actual - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        productos_pagina = self.controlador_tienda.productos[inicio:fin]

        # Agregar los productos a la tabla
        for producto in productos_pagina:
            self.tabla.insert("", END, values=(
                producto.get_nombre(),
                producto.get_descripcion(),
                f"${producto.get_precio():.2f}",  # Formatear el precio
                producto.get_stock(),
                producto.get_marca()
            ))

    def pagina_anterior(self):
        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.mostrar_pagina()

    def pagina_siguiente(self):
        total_paginas = (len(self.controlador_tienda.productos) // self.elementos_por_pagina )+ 1
        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.mostrar_pagina()