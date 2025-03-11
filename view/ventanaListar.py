from tkinter import Toplevel, Frame, BOTH, LEFT, RIGHT, Y, END
from tkinter import ttk

class VentanaListar:
    def __init__(self, root, controlador_tienda):
        self.root = root
        self.controlador_tienda = controlador_tienda

        self.ventana = Toplevel(self.root)
        self.ventana.title("Lista de Productos")
        self.ventana.geometry("850x450")  
        self.ventana.resizable(False, False)
        self.centrar_ventana(self.ventana)

        # Aplicar estilos personalizados
        self.estilizar_interfaz()

        # Contenedor principal
        contenedor = Frame(self.ventana, bg="#2C2F33", padx=10, pady=10)
        contenedor.pack(fill=BOTH, expand=True)

        # Frame para la tabla y la barra de desplazamiento
        frame_tabla = Frame(contenedor, bg="#2C2F33")
        frame_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Definir columnas
        columnas = ("Nombre", "Descripción", "Precio", "Stock", "Marca")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", style="TreeviewEstilizado")
        self.tabla.pack(side=LEFT, fill=BOTH, expand=True)

        # Configuración de columnas
        anchos_columnas = [180, 250, 90, 60, 120]
        for col, ancho in zip(columnas, anchos_columnas):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor="center")

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Frame para botones de paginación
        frame_paginacion = Frame(contenedor, bg="#2C2F33")
        frame_paginacion.pack(pady=10)

        self.pagina_actual = 1
        self.elementos_por_pagina = 10

        self.btn_anterior = ttk.Button(frame_paginacion, text="◄ Anterior", command=self.pagina_anterior, style="Boton.TButton")
        self.btn_anterior.pack(side=LEFT, padx=10)

        self.btn_siguiente = ttk.Button(frame_paginacion, text="Siguiente ►", command=self.pagina_siguiente, style="Boton.TButton")
        self.btn_siguiente.pack(side=LEFT, padx=10)

        # Mostrar primera página de datos
        self.mostrar_pagina()

    def estilizar_interfaz(self):
        #"""Aplica estilos personalizados"""
        estilo = ttk.Style()

        # Estilo para la tabla
        estilo.configure("TreeviewEstilizado",
                         font=("Arial", 10),
                         foreground="white",
                         background="#2C2F33",  
                         fieldbackground="#2C2F33",  
                         rowheight=28)

        estilo.configure("Treeview.Heading",
                         font=("Arial", 11, "bold"),
                         foreground="white",
                         background="#007ACC",
                         padding=5)

        estilo.map("Treeview", background=[("selected", "#005B99")])  

        # Estilo para los botones
        estilo.configure("Boton.TButton",
                         font=("Arial", 10, "bold"),
                         foreground="white",
                         background="#007ACC",
                         padding=7)
        estilo.map("Boton.TButton", background=[("active", "#005B99")])

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = 850
        alto = 450
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def mostrar_pagina(self):
        #"""Carga los datos en la tabla con paginación"""
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        if not hasattr(self.controlador_tienda, "productos") or len(self.controlador_tienda.productos) == 0:
            print("No hay productos en la tienda.")
            return

        inicio = (self.pagina_actual - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        productos_pagina = self.controlador_tienda.productos[inicio:fin]

        for producto in productos_pagina:
            self.tabla.insert("", END, values=(
                producto.get_nombre(),
                producto.get_descripcion(),
                f"${producto.get_precio():.2f}",
                producto.get_stock(),
                producto.get_marca()
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
