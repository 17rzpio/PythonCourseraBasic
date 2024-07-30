def maior_elemento(lista):
    x=lista[0]
    for n in lista:
        if(n>x):
            x=n
    return x