class Mensagem:
    def __init__(self):
        self.__tamanho = 100
        self.__bold = '\033[1m'
        self.__alerta = '\033[91m'
        self.__sucesso = '\033[92m'
        self.__info = '\033[94m'
        self.__end = '\033[0m'

    def titulo(self, titulo):
        print(chr(27) + "[2J")
        titulo = " {0} ".format(titulo.upper()).center(self.__tamanho, '*')
        print("\n {0} \n".format(titulo))

    def alerta(self, mensagem):
        if mensagem:
            print(
                self.__alerta + mensagem.center(self.__tamanho) + self.__end
            )

    def sucesso(self, mensagem):
        if mensagem:
            print(
                self.__sucesso + mensagem.center(self.__tamanho) + self.__end
            )

    def info(self, mensagem):
        if mensagem:
            print(
                self.__info + mensagem.center(self.__tamanho) + self.__end
            )
