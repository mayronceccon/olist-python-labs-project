import time
from models.mensagem import Mensagem
from models.correntista import Correntista as CorrentistaModel


class Correntista:
    def __init__(self):
        self.__mensagem = Mensagem()
        self.__nome = None
        self.__saldo = None

    def cadastrar(self):
        self.__mensagem.mensagens(
            titulo="Cadastrar Correntista"
        )
        self.__mensagem.print()

        try:
            if not self.__nome:
                self.__nome = str(input("Nome: "))

            if not self.__saldo:
                self.__saldo = float(input("Depósito inicial: R$ "))

            correntista = CorrentistaModel(
                self.__nome,
                self.__saldo
            )

            self.__mensagem.mensagens(
                sucesso="Correntista {0} cadastrado com sucesso".format(
                    self.__nome
                ),
                info="Você será redirecionado para tela inicial. Aguarde..."
            )
            self.__mensagem.print()
            time.sleep(2)
            return correntista
        except ValueError:
            self.__mensagem.mensagens(
                alerta="Preencha novamente o dado corretamente!"
            )
            return self.cadastrar()
        except Exception:
            self.__mensagem.mensagens(
                alerta="Tente novamente em alguns instantes!"
            )
            return self.cadastrar()

    def selecionar(self, correntistas):
        self.__mensagem.mensagens(
            titulo="Selecionar Correntista"
        )
        self.__mensagem.print()

        try:
            for (id, correntista) in enumerate(correntistas):
                print("{0} - {1}".format(id, correntista.nome()))

            opcao = int(input())
            return correntistas[opcao]
        except (ValueError, IndexError):
            self.__mensagem.mensagens(
                alerta="Erro ao selecionar o correntista!"
            )
            return self.selecionar(correntistas)
