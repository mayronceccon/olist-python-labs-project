from models.mensagem import Mensagem
from views.correntista import Correntista as CorrentistaView
from views.historico import Historico as HistoricoView
from models.correntista import Correntista as CorrentistaModel
from models.registros_auditoria import RegistroAuditoria


class Principal:
    def __init__(self):
        self.__mensagem = Mensagem()
        self.__registros_auditoria = RegistroAuditoria()
        self.__correntista = None
        self.__correntistas = []
        self.__titulo = None
        self.__alerta = None
        self.__sucesso = None

        self.__mensagem.mensagens(
            titulo="Sistema Bancário"
        )

    def inicial(self):
        self.__mensagem.print()

        try:
            messagem = (
                "Escolha uma opção abaixo:\n"
                "0 - Sair\n" +
                "1 - Cadastro de novo correntista\n" +
                "2 - Selecionar correntista\n" +
                "3 - Auditoria"
            )
            print(messagem)
            opcao = int(input())

            opcoes_validas = [0, 1, 2, 3]
            if opcao not in opcoes_validas:
                raise ValueError

            if opcao == 0:
                self.__sair()

            if opcao == 1:
                self.__correntistas.append(
                    CorrentistaView(self.__registros_auditoria).cadastrar()
                )
                return self.inicial()

            if opcao == 2:
                if not self.__correntistas:
                    self.__mensagem.mensagens(
                        alerta="Nenhum correntista encontrado! Faça o cadastro!"
                    )
                    return self.inicial()
                self.__correntista = CorrentistaView(
                    self.__registros_auditoria
                ).selecionar(
                    self.__correntistas
                )
                self.__mensagem.mensagens(
                    titulo="Área do cliente",
                    sucesso="Correntista selecionado..."
                )
                return self.dashboard()

            if opcao == 3:
                auditorias = self.__registros_auditoria.relatorio()
                for auditoria in auditorias:
                    print(auditorias[auditoria])
                input()
                return self.inicial()
        except ValueError:
            self.__mensagem.mensagens(
                alerta="Opção inválida! Informe uma opção válida!"
            )
            return self.inicial()

    def dashboard(self):
        self.__mensagem.print()

        try:
            messagem = (
                "Correntista: {0}\n".format(self.__correntista.nome()) +
                "Saldo: {0}\n".format(self.__correntista.saldo()) +
                "\n" +
                "Operações\n" +
                "=" * 10 + "\n" +
                "1 - Fazer Depósito\n" +
                "2 - Fazer Saque\n" +
                "3 - Ver Histórico\n" +
                "4 - Sair\n"
            )
            print(messagem)

            opcao = int(input())

            opcoes_validas = [1, 2, 3, 4]
            if opcao not in opcoes_validas:
                raise ValueError

            if opcao == 4:
                self.inicial()

            if opcao == 1:
                valor_deposito = float(input("Informe o valor do depósito: R$ "))
                self.__correntista.depositar(valor_deposito)

                mensagem = "Depósito de R$ {0} efetuado com sucesso".format(
                    valor_deposito
                )
                self.__mensagem.mensagens(
                    sucesso=mensagem
                )
                return self.dashboard()

            if opcao == 2:
                valor_saque = float(input("Informe o valor do saque: R$ "))
                self.__correntista.sacar(valor_saque)
                mensagem = "Saque de R$ {0} efetuado com sucesso".format(
                    valor_saque
                )
                self.__mensagem.mensagens(
                    sucesso=mensagem
                )
                return self.dashboard()

            if opcao == 3:
                historico = HistoricoView(self.__correntista)
                historico.relatorio()
                return self.dashboard()
        except ValueError:
            self.__mensagem.mensagens(
                alerta="Opção inválida! Informe uma opção válida!"
            )
            return self.dashboard()

    def __sair(self):
        self.__mensagem.mensagens(
            sucesso="Saindo... Obrigado por utilizar nosso sistema!"
        )
        self.__mensagem.print()
        exit(0)
