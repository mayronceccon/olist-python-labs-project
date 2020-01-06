
class Correntista:
    def __init__(self, historico):
        self.__historico = historico
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__historico.listar()) - 1:
            raise StopIteration
        historico = self.__historico.listar()[self.__index]
        self.__index += 1
        return historico
