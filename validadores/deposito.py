from validadores.regras.valor import Valor as ValidacaoValor
from validadores.regras.valor_negativo import ValorNegativo as ValidacaoValorNegativo


class Deposito():
    def __init__(self, valor=0):
        ValidacaoValor(valor).is_valid()
        ValidacaoValorNegativo(valor).is_valid()
