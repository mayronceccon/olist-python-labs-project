from contextlib import suppress


class Mensagem:
    def __init__(self):
        self.__tamanho = 100
        self.__cores()
        self.__limpar_mensagens()
        self.__mensagem_titulo = None

    def __limpar_mensagens(self):
        self.__mensagem_alerta = None
        self.__mensagem_sucesso = None
        self.__mensagem_info = None

    def __cores(self):
        self.__cor_alerta = '\033[91m'
        self.__cor_sucesso = '\033[92m'
        self.__cor_info = '\033[94m'
        self.__cor_end = '\033[0m'

    def print(self):
        print(chr(27) + "[2J")
        if self.__mensagem_titulo:
            print(self.__mensagem_titulo)

        if self.__mensagem_alerta:
            print(self.__mensagem_alerta)

        if self.__mensagem_sucesso:
            print(self.__mensagem_sucesso)

        if self.__mensagem_info:
            print(self.__mensagem_info)

        self.__limpar_mensagens()

    def mensagens(self, **kwargs):
        with suppress(KeyError):
            self.titulo(kwargs['titulo'])

        with suppress(KeyError):
            self.sucesso(kwargs['sucesso'])

        with suppress(KeyError):
            self.alerta(kwargs['alerta'])

        with suppress(KeyError):
            self.info(kwargs['info'])

    def titulo(self, titulo):
        if titulo:
            titulo = " {0} " \
                .format(titulo.upper()) \
                .center(self.__tamanho, '#')
            self.__mensagem_titulo = "\n{0}\n".format(titulo)

    def alerta(self, alerta):
        if alerta:
            self.__mensagem_alerta = self.__cor_alerta \
                + alerta.center(self.__tamanho) \
                + self.__cor_end

    def sucesso(self, sucesso):
        if sucesso:
            self.__mensagem_sucesso = self.__cor_sucesso \
                + sucesso.center(self.__tamanho) \
                + self.__cor_end

    def info(self, info):
        if info:
            self.__mensagem_info = self.__cor_info \
                + info.center(self.__tamanho) \
                + self.__cor_end
