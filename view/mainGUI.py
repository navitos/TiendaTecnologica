from tkinter import *

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda")
        self.root.minsize(width=600, height=400)

        self.frame_botones = Frame(self.root)
        self.frame_botones.grid(row=0, column=0, sticky="nw")

        self.crear_menus()
        self.crear_botones()
    
    def crear_menus(self):
        self.menu_celular = Menu(self.root, tearoff=0)
        self.menu_celular.add_command(label="Añadir celular", command=self.abrir_ventana_celular)
        self.menu_celular.add_command(label="Consultar celular")
        self.menu_celular.add_command(label="Eliminar celular")

        self.menu_computador = Menu(self.root, tearoff=0)
        self.menu_computador.add_command(label="Añadir computador", command=self.abrir_ventana_computador)
        self.menu_computador.add_command(label="Consultar computador")
        self.menu_computador.add_command(label="Eliminar computador")

    def crear_botones(self):
        self.btn_celular = Button(self.frame_botones, text="Celular", 
                                  command=lambda: self.mostrar_menu_bajo_boton(self.btn_celular, self.menu_celular))
        self.btn_celular.grid(row=0, column=0, sticky="w")

        self.btn_computador = Button(self.frame_botones, text="Computador", 
                                     command=lambda: self.mostrar_menu_bajo_boton(self.btn_computador, self.menu_computador))
        self.btn_computador.grid(row=0, column=1, sticky="w")

        self.btn_listar = Button(self.frame_botones, text="Listar")
        self.btn_calcular = Button(self.frame_botones, text="Calcular Precio")
        self.btn_acerca = Button(self.frame_botones, text="Acerca de", command=self.abrir_ventana_acerca)

        self.btn_listar.grid(row=0, column=2, sticky="w")
        self.btn_calcular.grid(row=0, column=3, sticky="w")
        self.btn_acerca.grid(row=0, column=4, sticky="w")
    
    def mostrar_menu_bajo_boton(self, boton, menu):
        x = boton.winfo_rootx()
        y = boton.winfo_rooty() + boton.winfo_height()
        menu.tk_popup(x, y)

    def abrir_ventana_acerca(self):
        nueva_ventana = Toplevel(self.root)
        nueva_ventana.title("Menú acerca de")
        nueva_ventana.minsize(width=300, height=200)
        Label(nueva_ventana, text="David Alejandro Gutiérrez Hernández - 2220211001").pack(pady=5)
        Label(nueva_ventana, text="Julián Rubiano Santofimio - 2220211015").pack(pady=5)
        Label(nueva_ventana, text="David Alejandro De Los Reyes Ostos - 2220221059").pack(pady=5)
        Label(nueva_ventana, text="Jose Ariel Reséndiz Perez").pack(pady=5)

    def abrir_ventana_celular(self):
        FormularioCelular(self.root)

    def abrir_ventana_computador(self):
        FormularioComputador(self.root)

if __name__ == "__main__":
    root = Tk()
    app = TiendaApp(root)
    root.mainloop()