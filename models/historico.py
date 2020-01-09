from datetime import datetime


class Historico:
    DEPOSITO = "C"
    SAQUE = "D"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, value):
        self.__mensagem = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

    @property
    def tipo_operacao(self):
        return self.__tipo_operacao

    @tipo_operacao.setter
    def tipo_operacao(self, value):
        self.__tipo_operacao = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value
