class EmpresaProTec:
    """
    Implementa el patrón Singleton para la empresa.
    """
    _instance = None

    def __new__(cls, nit, nombre, razon_social):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(nit, nombre, razon_social)  # Inicializa la instancia
        return cls._instance

    def __init__(self, nit, nombre, razon_social):
        if not hasattr(self, 'nit'):  # Evita sobrescribir los atributos si ya existen
            self.nit = nit
            self.nombre = nombre
            self.razon_social = razon_social