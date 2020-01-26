import unittest
from models.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.nome = "Mayron"
        self.cpf = "01234567890"
        self.pessoa = Pessoa(
            self.nome,
            self.cpf
        )

    def test_verificar_instancia(self):
        self.assertIsInstance(self.pessoa, Pessoa)

    def test_exception_nao_informados_parametros(self):
        with self.assertRaises(TypeError):
            pessoa = Pessoa()

    def test_retorno_str(self):
        esperado = "{0} - {1}".format(
            self.nome,
            self.cpf
        )
        self.assertEqual(esperado, str(self.pessoa))

    def test_retorno_dos_dados(self):
        self.assertEqual(self.nome, self.pessoa.nome())
        self.assertEqual(self.cpf, self.pessoa.cpf())
