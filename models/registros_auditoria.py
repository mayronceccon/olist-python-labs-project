from models.auditoria import Auditoria
from models.pessoa import Pessoa


class RegistroAuditoria:
    def __init__(self):
        self.__auditorias = {}

    def inserir(self, cpf, auditoria):
        if not isinstance(auditoria, Auditoria):
            raise TypeError("Auditoria inválida")

        if cpf not in self.__auditorias:
            self.__auditorias[cpf] = []

        element = self.__auditorias[cpf]
        element.append(auditoria)
        self.__auditorias.update({cpf: element})

    def relatorio(self, cpf=None):
        if cpf:
            return self.__auditorias[cpf]
        return self.__auditorias
