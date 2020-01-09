from models.mensagem import Mensagem
from models.correntista import Correntista
from models.historico import Historico as HistoricoData


class Historico:
    def __init__(self, correntista):
        if not isinstance(correntista, Correntista):
            raise TypeError("Correntista não selecionado")

        self.__mensagem = Mensagem()
        self.__correntista = correntista

    def relatorio(self):
        self.__mensagem.mensagens(
            titulo="Histórico",
            info="Histórico do correntista {0}".format(
                self.__correntista.nome()
            )
        )
        self.__mensagem.print()

        historico_correntista = self.__correntista

        tamanho_mensagem = max([len(l.mensagem) for l in lista])
        tamanho_valor = max([len(str(format(float(l.valor), '.2f'))) for l in lista])
        tamanho_saldo = max([len(str(format(float(l.saldo), '.2f'))) for l in lista])

        print("\n")
        for hist in historico_correntista:
            tipo_operacao = hist.tipo_operacao
            cor_valor = '\033[94m'
            if tipo_operacao == HistoricoData.SAQUE:
                cor_valor = '\033[91m'
            elif tipo_operacao == HistoricoData.DEPOSITO:
                cor_valor = '\033[92m'

            valor = format(float(hist.valor), '.2f')
            valor = cor_valor + valor + '\033[0m'
            saldo = format(float(hist.saldo), '.2f')

            info = "|{data}|{mensagem}|{valor}|{operacao}|{saldo}|".format(
                data=hist.data.strftime("%d/%m/%Y %H:%M:%S"),
                mensagem=hist.mensagem.ljust(tamanho_mensagem),
                valor=valor.ljust(tamanho_valor + 9),
                operacao=tipo_operacao,
                saldo=saldo.ljust(tamanho_saldo)
            )
            print(info)
        print("\n")
        print(input("Pressione enter para voltar"))
