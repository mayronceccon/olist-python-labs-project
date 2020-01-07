from correntista import Correntista

if __name__ == '__main__':
    print(Correntista, Correntista.__doc__)
    correntista = Correntista("Mayron", 500)
    print(correntista)

    print(correntista.nome())
    print(correntista.saldo())

    correntista.depositar(25.50)
    correntista.sacar(20.50)
    correntista.sacar(10.50)
    correntista.sacar(100.50)
    correntista.depositar(925.50)

    for hist in correntista:
        print(hist)

    print(correntista.saldo())

    print("-" * 40)

    correntista = Correntista("Helloíse", 100)
    print(correntista)

    print(correntista.nome())
    print(correntista.saldo())

    correntista.depositar(100)
    correntista.depositar(100.50)

    for hist in correntista:
        print(hist)

    print(correntista.saldo())
