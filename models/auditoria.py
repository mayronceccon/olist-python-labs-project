from datetime import datetime
from models.pessoa import Pessoa
from models.conta import Conta


class Auditoria:
    def __init__(self, pessoa, conta):
        if not isinstance(pessoa, Pessoa):
            raise TypeError("Pessoa inválida")

        if not isinstance(conta, Conta):
            raise TypeError("Conta inválida")

        self.__pessoa = pessoa
        self.__conta = conta
        self.__tipo = None
        self.__operacao = None
        self.__data_inicio = None
        self.__data_fim = None
        self.__status = None
        self.__valor = 0

    def pessoa(self):
        return self.__pessoa

    def data_inicio(self):
        return self.__data_inicio

    def data_fim(self):
        return self.__data_fim

    def operacao(self):
        return self.__operacao

    def valor(self):
        return self.__valor

    def iniciar_processo(self, tipo, valor):
        self.__data_inicio = datetime.now()
        self.__tipo = tipo
        self.__valor = valor

    def finalizar_processo(self, status):
        if not isinstance(status, str):
            raise TypeError("Status inválido")

        try:
            self.__status = status
            self.__data_fim = datetime.now()
        except IndexError:
            raise IndexError("Processo não encontrado")
