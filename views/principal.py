from models.mensagem import Mensagem
from views.correntista import Correntista as CorrentistaView
from models.correntista import Correntista as CorrentistaModel


class Principal:
    def __init__(self):
        self.__mensagem = Mensagem()
        self.__correntista = None
        self.__correntistas = []

    def inicial(self):
        try:
            messagem = (
                "Escolha uma opção abaixo:\n"
                "0 - Sair\n" +
                "1 - Cadastro de novo correntista\n" +
                "2 - Selecionar correntista"
            )
            print(messagem)
            opcao = int(input())

            opcoes_validas = [0, 1, 2]
            if opcao not in opcoes_validas:
                raise ValueError

            if opcao == 0:
                self.__sair()

            if opcao == 1:
                self.__correntistas.append(CorrentistaView().cadastrar())
                return self.inicial()

            if opcao == 2:
                if not self.__correntistas:
                    self.__mensagem.alerta(
                        "Nenhum correntista encontrado! Faça o cadastro!"
                    )
                    self.inicial()
                self.__correntista = CorrentistaView().selecionar(
                    self.__correntistas
                )
                return self.dashboard()

        except ValueError:
            self.__mensagem.titulo("ERRO NA OPERAÇÃO")
            self.__mensagem.alerta("Opção inválida! Informe uma opção válida!")
            return self.inicial()

    def dashboard(self):
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
                self.__sair()

            if opcao == 1:
                valor_deposito = float(input("Informe o valor do depósito: R$ "))
                self.__correntista.depositar(valor_deposito)
                return self.dashboard()

            if opcao == 2:
                valor_saque = float(input("Informe o valor do saque: R$ "))
                self.__correntista.sacar(valor_saque)
                return self.dashboard()

            if opcao == 3:
                self.__mensagem.titulo("Histórico")
                for hist in self.__correntista:
                    print(hist)
                return self.dashboard()

        except ValueError:
            self.__mensagem.titulo("ERRO NA OPERAÇÃO")
            self.__mensagem.alerta("Opção inválida! Informe uma opção válida!")
            return self.dashboard()

    def __sair(self):
        self.__mensagem.titulo("SAINDO")
        self.__mensagem.alerta("Obrigado por utilizar nosso sistema!")
        exit(0)
