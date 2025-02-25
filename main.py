from tkinter import Tk
from view.mainGUI import TiendaApp
from view.formularioCelular import FormularioCelular
from view.formularioComputador import FormularioComputador
from services.controladorTienda import ControladorTienda
from model.celular import Celular
from model.computador import Computador
from model.monitor import Monitor


if __name__ == "__main__":
    root = Tk()
    app = TiendaApp(root)
    root.mainloop()