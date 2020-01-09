from models.mensagem import Mensagem
from views.principal import Principal as PrincipalView

mensagem = Mensagem()


def sair():
    mensagem.titulo("Saindo...")
    mensagem.alerta("Obrigado por utilizar nosso sistema!")
    exit()


if __name__ == '__main__':
    try:
        principal = PrincipalView()
        principal.inicial()
    except Exception:
        mensagem.titulo("ERRO NA OPERAÇÃO")
        mensagem.alerta("Um erro ocorreu entre em contato com nossa central!")
    except KeyboardInterrupt:
        sair()
