class Observable:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

    def actualizar(self):
        print(f"Notificación recibida")  # Puedes actualizar la UI aquí 