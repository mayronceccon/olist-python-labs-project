from .regra import Regra


class SaldoInsulficiente(Regra):
    def __init__(self, saldo, valor):
        self.__saldo = float(saldo)
        self.__valor = float(valor)

    def is_valid(self):
        if (self.__saldo - self.__valor < 0):
            raise Exception('Saldo insulficiente para saque')
