from validadores.regras.valor import Valor as ValidacaoValor
from validadores.regras.valor_negativo import ValorNegativo as ValidacaoValorNegativo
from validadores.regras.saldo_insulficiente import SaldoInsulficiente


class Saque():
    def __init__(self, saldo=0, valor=0):
        ValidacaoValor(valor).is_valid()
        ValidacaoValorNegativo(valor).is_valid()
        SaldoInsulficiente(saldo, valor).is_valid()
