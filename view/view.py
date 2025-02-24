from tkinter import *

def mostrar_menu_bajo_boton(boton, menu):
    x = boton.winfo_rootx()
    y = boton.winfo_rooty() + boton.winfo_height()
    menu.tk_popup(x, y)

def abrir_ventana_acerca():
    nueva_ventana = Toplevel(ventanaPrincipal)
    nueva_ventana.title("Menú acerca de")
    nueva_ventana.minsize(width=300, height=200)
    Label(nueva_ventana, text="David Alejandro Gutiérrez Hernández - 2220211001").pack(pady=5)
    Label(nueva_ventana, text="Julián Rubiano Santofimio - 2220211015").pack(pady=5)
    Label(nueva_ventana, text="David Alejandro De Los Reyes Ostos - 2220221059").pack(pady=5)
    Label(nueva_ventana, text="Jose Ariel Reséndiz Perez").pack(pady=5)

def abrir_ventana_celular():
    nueva_ventana = Toplevel(ventanaPrincipal)
    nueva_ventana.title("Añadir Celular")
    nueva_ventana.minsize(width=300, height=350)
    
    Label(nueva_ventana, text="Nombre:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Stock:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Precio:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Marca:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Tamaño:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Fecha de lanzamiento:").pack()
    Entry(nueva_ventana).pack()
    
    Button(nueva_ventana, text="Guardar").pack(pady=10)

def abrir_ventana_computador():
    nueva_ventana = Toplevel(ventanaPrincipal)
    nueva_ventana.title("Añadir Computador")
    nueva_ventana.minsize(width=300, height=350)
    
    Label(nueva_ventana, text="Nombre:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Stock:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Precio:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Marca:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="Tarjeta Gráfica:").pack()
    Entry(nueva_ventana).pack()
    Label(nueva_ventana, text="RAM:").pack()
    Entry(nueva_ventana).pack()
    
    Button(nueva_ventana, text="Guardar").pack(pady=10)

ventanaPrincipal = Tk()
ventanaPrincipal.title("Tienda")
ventanaPrincipal.minsize(width=600, height=400)

frame_botones = Frame(ventanaPrincipal)
frame_botones.grid(row=0, column=0, sticky="nw")

menu_celular = Menu(ventanaPrincipal, tearoff=0)
menu_celular.add_command(label="Añadir celular", command=abrir_ventana_celular)
menu_celular.add_command(label="Consultar celular")
menu_celular.add_command(label="Eliminar celular")

menu_computador = Menu(ventanaPrincipal, tearoff=0)
menu_computador.add_command(label="Añadir computador", command=abrir_ventana_computador)
menu_computador.add_command(label="Consultar computador")
menu_computador.add_command(label="Eliminar computador")

btn_celular = Button(frame_botones, text="Celular", command=lambda: mostrar_menu_bajo_boton(btn_celular, menu_celular))
btn_celular.grid(row=0, column=0, sticky="w")

btn_computador = Button(frame_botones, text="Computador", command=lambda: mostrar_menu_bajo_boton(btn_computador, menu_computador))
btn_computador.grid(row=0, column=1, sticky="w")

btn_listar = Button(frame_botones, text="Listar")
btn_calcular = Button(frame_botones, text="Calcular Precio")
btn_acerca = Button(frame_botones, text="Acerca de", command=abrir_ventana_acerca)

btn_listar.grid(row=0, column=2, sticky="w")
btn_calcular.grid(row=0, column=3, sticky="w")
btn_acerca.grid(row=0, column=4, sticky="w")

ventanaPrincipal.mainloop()
