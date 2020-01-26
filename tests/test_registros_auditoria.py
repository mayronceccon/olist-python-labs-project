import unittest
from unittest.mock import Mock
from models.registros_auditoria import RegistroAuditoria
from models.auditoria import Auditoria
from models.pessoa import Pessoa
from models.conta import Conta
from models.tipo_auditoria import TipoAuditoria
from models.status_auditoria import StatusAuditoria


class TestRegistrosAuditoria(unittest.TestCase):
    def setUp(self):
        self.__cpf = "01234567890"

    def test_inserir_auditoria_invalida(self):
        registros = RegistroAuditoria()
        with self.assertRaises(TypeError):
            registros.inserir(self.__cpf, None)

    def test_inserir_auditoria(self):
        auditoria = Mock(spec=Auditoria)
        registros = RegistroAuditoria()
        registros.inserir(self.__cpf, auditoria)

    def test_lista_de_auditorias(self):
        registros = RegistroAuditoria()

        auditoria = Mock(spec=Auditoria)
        registros.inserir(self.__cpf, auditoria)

        auditoria = Mock(spec=Auditoria)
        registros.inserir(self.__cpf, auditoria)

        auditoria = Mock(spec=Auditoria)
        registros.inserir(self.__cpf, auditoria)

        auditorias_realizadas = registros.relatorio()
        self.assertIsInstance(auditorias_realizadas, dict)
        self.assertEqual(1, len(auditorias_realizadas))

        auditorias_realizadas = registros.relatorio(self.__cpf)
        self.assertIsInstance(auditorias_realizadas, list)
        self.assertEqual(3, len(auditorias_realizadas))
        self.assertIsInstance(auditorias_realizadas[0], Auditoria)
