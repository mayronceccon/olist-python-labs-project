import unittest
from unittest.mock import Mock
from datetime import datetime
from models.pessoa import Pessoa
from models.conta import Conta
from models.auditoria import Auditoria
from models.tipo_auditoria import TipoAuditoria
from models.status_auditoria import StatusAuditoria


class TestAuditoria(unittest.TestCase):
    def setUp(self):

        self.tipo_auditoria = Mock(spec=TipoAuditoria)
        self.tipo_auditoria.DEPOSITO = "D"
        self.tipo_auditoria.SAQUE = "S"

        self.status_auditoria = Mock(spec=StatusAuditoria)
        self.status_auditoria.CONCLUIDO = "OK"
        self.status_auditoria.NAO_CONCLUIDO = "NOK"

        self.pessoa = Mock(spec=Pessoa)
        self.conta = Mock(spec=Conta)

    def test_instancia_da_classe(self):
        with self.assertRaises(TypeError):
            auditoria = Auditoria("mayron")

        with self.assertRaises(TypeError):
            auditoria = Auditoria(
                self.pessoa,
                "01234567890"
            )

        auditoria = Auditoria(
            self.pessoa,
            self.conta
        )

    def test_atributos_none(self):
        auditoria = Auditoria(
            self.pessoa,
            self.conta
        )

        self.assertIsNone(auditoria.data_inicio())
        self.assertIsNone(auditoria.data_fim())
        self.assertIsNone(auditoria.operacao())

    def test_iniciar_auditoria(self):
        auditoria = Auditoria(
            self.pessoa,
            self.conta
        )

        auditoria.iniciar_processo(
            self.tipo_auditoria.DEPOSITO,
            20
        )
        self.assertIsInstance(auditoria.data_inicio(), datetime)

    def test_finalizar_processo(self):
        auditoria = Auditoria(
            self.pessoa,
            self.conta
        )

        status = StatusAuditoria.CONCLUIDO
        auditoria.iniciar_processo(
            self.tipo_auditoria.DEPOSITO,
            20
        )

        auditoria.finalizar_processo(
            self.status_auditoria.CONCLUIDO
        )
        self.assertIsInstance(auditoria.data_fim(), datetime)
