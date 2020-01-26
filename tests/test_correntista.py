import unittest
from unittest.mock import Mock
from models.pessoa import Pessoa
from models.conta import Conta
from models.correntista import Correntista
from models.auditoria import Auditoria


class TestCorrentista(unittest.TestCase):
    def setUp(self):
        self.pessoa = Mock(spec=Pessoa)
        self.pessoa.nome.return_value = "Mayron"
        self.pessoa.cpf.return_value = "07785679908"

        self.conta = Mock(spec=Conta)
        self.conta.saldo.return_value = 1000

        self.auditoria = Mock(spec=Auditoria)

    def test_instancia_da_classe(self):
        with self.assertRaises(TypeError):
            Correntista("Mayron", self.conta)

        with self.assertRaises(TypeError):
            Correntista(self.pessoa, 1000)

    def test_sacar_valor(self):
        correntista = Correntista(self.pessoa, self.conta)
        correntista.sacar(20, self.auditoria)

        self.auditoria.inserir.assert_called_once_with(
            self.pessoa.cpf(),
            self.auditoria
        )

        self.conta.saldo.return_value = 980
        self.assertEqual(980, correntista.saldo())
