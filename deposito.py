from validadores.deposito import Deposito as ValidacaoDeposito


class Deposito:
    def __init__(self, conta, valor):
        self.__conta = conta
        self.__valor = float(valor)
        self.__validar()
        self.__set_saldo()

    def saldo(self):
        return self.__saldo

    def __set_saldo(self):
        self.__saldo = float(self.__conta.saldo()) + float(self.__valor)

    def __validar(self):
        ValidacaoDeposito(self.__valor)
