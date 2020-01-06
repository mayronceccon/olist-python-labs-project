class Historico:
    def __init__(self):
        self.__historicos = []

    def inserir(self, historico):
        self.__historicos.append(historico)

    def listar(self):
        return self.__historicos
