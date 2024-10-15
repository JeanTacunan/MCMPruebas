from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCD(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        return self.MCDMasDosNumeros()

    def MCD(self, numero1, numero2):
        while numero2 != 0:
            numero1, numero2 = numero2, numero1 % numero2
        return numero1

    def MCDMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los números deben ser enteros")

        cantidadNumeros = len(self.__numeros)
        mcd = self.MCD(self.__numeros[0], self.__numeros[1])
        for i in range(2, cantidadNumeros):
            mcd = self.MCD(mcd, self.__numeros[i])
        return mcd

    def MCM(self, numero1, numero2):
        return abs(numero1 * numero2) // self.MCD(numero1, numero2)

    def MCMMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los números deben ser enteros")

        cantidadNumeros = len(self.__numeros)
        mcm = self.MCM(self.__numeros[0], self.__numeros[1])
        for i in range(2, cantidadNumeros):
            mcm = self.MCM(mcm, self.__numeros[i])
        return mcm

    def calcularMCM(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        return self.MCMMasDosNumeros()
