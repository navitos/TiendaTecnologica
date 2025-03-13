class EmpresaProTec:
    """
    Implementa el patrón Singleton para la empresa.
    """
    _instance = None

    def __new__(cls, nit, nombre, razon_social):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nit = nit
            cls._instance.nombre = nombre
            cls._instance.razon_social = razon_social
        return cls._instance

    def __init__(self, nit, nombre, razon_social):
        pass