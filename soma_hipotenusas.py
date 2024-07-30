def é_hipotenusa(n):
    cateto1=1
    while(cateto1<n):
        cateto2=1
        while(cateto2<n):
            if((n%((cateto1*cateto1+cateto2*cateto2)**(1/2)))==0):
                return True
            cateto2+=1
        cateto1+=1
    return False

def soma_hipotenusas(n):
    cont=0
    cont2=0
    while(cont<=n):
        if(é_hipotenusa(cont)==True):
           cont2+=cont
        cont+=1
    return cont2

def main():
    n=int(input("digite qual valor a calcular"))
    soma_hipotenusas(n)

main()