corretistas = []


def set_correntista(correntista):
    global correntistas
    correntistas.append(correntista)


def get_correntista(cpf):
    return corretistas[0]
