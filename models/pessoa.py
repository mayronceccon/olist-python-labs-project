class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf

    def __str__(self):
        return "{nome} - {cpf}".format(
            nome=self.nome(),
            cpf=self.cpf()
        )
