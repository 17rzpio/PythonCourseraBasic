def main():
    numero = 0
    while ( numero <= 0 ):
        numero = int ( input ( " Digite o valor de um numero inteiro n > 0 até 4 digitos " ) )

    digito = int ( input (" Digite o valor de digito d ( 0<=d<=9): "))
    while (digito<0):
        digito = int ( input (" Digite o valor de digito d ( 0<=d<=9): "))
    while (digito>9):
        digito = int ( input (" Digite o valor de digito d ( 0<=d<=9): "))

    comprimento = len(numero)
    quantidadedezena = comprimento
    quantidadedigito = 0
    quantidadedigitomilhar = 1

    if(comprimento == 1):
        if(digito == numero):
            quantidadedigito +=1
