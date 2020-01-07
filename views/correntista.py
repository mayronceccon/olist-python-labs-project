import time
from models.mensagem import Mensagem
from models.correntista import Correntista as CorrentistaModel


class Correntista:
    def __init__(self):
        self.__mensagem = Mensagem()
        self.__nome = None
        self.__saldo = None

    def cadastrar(self):
        try:
            self.__mensagem.titulo("Cadastrar novo Correntista")

            if not self.__nome:
                self.__nome = str(input("NOME: "))

            if not self.__saldo:
                self.__saldo = float(input("SALDO: R$ "))

            self.__mensagem.titulo("Cadastro realizado com sucesso!")
            correntista = CorrentistaModel(
                self.__nome,
                self.__saldo
            )

            self.__mensagem.sucesso(
                "Correntista {0} cadastrado com sucesso".format(self.__nome)
            )

            self.__mensagem.info(
                "\nAguarde, você será direcionado para a tela inicial...\n"
            )
            time.sleep(5)
            return correntista
        except ValueError:
            self.__mensagem.titulo("Erro na operação de cadastro!")
            self.__mensagem.alerta("Preencha novamente o dado inválido!")
            return self.cadastrar()
        except Exception:
            self.__mensagem.titulo("Erro na operação de cadastro!")
            self.__mensagem.alerta("Tente novamente em alguns instantes!")

    def selecionar(self, correntistas):
        self.__mensagem.titulo("Busca de correntistas")

        for (id, correntista) in enumerate(correntistas):
            print("{0} - {1}".format(id, correntista.nome()))

        opcao = int(input())
        return correntistas[opcao]
