from models.historico import Historico


class HistoricoRelatorio:
    def __init__(self):
        self.__historicos = []

    def inserir(self, historico):
        if not isinstance(historico, Historico):
            raise TypeError("Tipo de histórico não suportado")
        self.__historicos.append(historico)

    def listar(self):
        return self.__historicos
