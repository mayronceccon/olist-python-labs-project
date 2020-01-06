from .regra import Regra


class ValorNegativo(Regra):
    def __init__(self, valor):
        self.__valor = float(valor)

    def is_valid(self):
        if self.__valor < 0:
            raise Exception('Valores negativos não são permitidos')
