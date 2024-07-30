def primos(incognita):
    cont=incognita
    cont2=0
    while(cont>1):
        if(incognita%cont==0):
            cont2+=1
            if(cont2==2):
                return False
        cont-=1
    return True

def n_primos(n):
    cont=1
    while(n>2):
        possibilidade=primos(n)
        if(possibilidade==True):
            cont+=1
        n-=1
    return cont

