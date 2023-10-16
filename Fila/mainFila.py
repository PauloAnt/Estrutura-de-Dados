from Fila import Fila, FilaException

f = Fila(5)
try:
    print(f.estaCheia())
    print(f.estaVazia())
    print(f.tamanho())
    print(f.enfileira(1))
    print(f.enfileira(2))
    print(f.enfileira(3))
    print(f.desenfileira())
    print(f.frente())
    print(f.__dict__)
    print(f.desenfileira())
    print(f.desenfileira())
    print(f.enfileira(1))
    print(f.enfileira(2))
    print(f.enfileira(3))
    print(f.enfileira(4))
    print(f.enfileira(5))
    print(f.__dict__)
    print(f.frente())
    print(f.busca(5))
    print(f.elemento(5))
    print(f.ultimo())
    print(f)
    while (not f.estaVazia()):
        print(f.desenfileira())
except FilaException as fe:
    print(fe)
except BaseException as be:
    print(be)