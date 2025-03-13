from view.ventanaListar import VentanaListar
from view.ventanaListarCelulares import VentanaListarCelulares
from view.ventanaListarComputadores import VentanaListarComputadores


class Observable:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, mensaje):

        for observador in self._observadores:
            if isinstance(observador, VentanaListar):
                observador.actualizar(mensaje)

    def notificar_observadores_computador(self, mensaje):

        for observador in self._observadores:
            if isinstance(observador, VentanaListarComputadores):
                observador.actualizar(mensaje)

    def notificar_observadores_celular(self, mensaje):

        for observador in self._observadores:
            if isinstance(observador, VentanaListarCelulares):
                observador.actualizar(mensaje)

    def actualizar(self):
        print(f"Notificación recibida")  # Puedes actualizar la UI aquí 