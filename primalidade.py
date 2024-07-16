print("Digite um número inteiro: ")
numero_digitado = int(input())

for i in range(1,numero_digitado+1):
    if(numero_digitado//i==0):
        print("nao eh primo")
        break
    else:
        if(i==numero_digitado):
            print("eh primo")
    
