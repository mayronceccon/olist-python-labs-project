from .regra import Regra


class Valor(Regra):
    def __init__(self, valor):
        self.__valor = float(valor)

    def is_valid(self):
        if type(self.__valor) is not float and type(self.__valor) is not int:
            raise Exception('Valor inválido')
