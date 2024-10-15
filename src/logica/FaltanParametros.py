class FaltanParametros(Exception):
    """Excepción personalizada para indicar que faltan parámetros."""

    def __init__(self, message="Se requieren al menos dos números para calcular MCD o MCM."):
        self.message = message
        super().__init__(self.message)
