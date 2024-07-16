def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''
    if(k==0):
        return 1
    if(k == 1):
        return 1

    # COMPLETE ESSA FUNÇÃO

    return k*(fatorial(k-1))

# testes
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("17! =", fatorial(17))

