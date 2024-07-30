def primo(incognita):
    cont=incognita
    cont2=0
    while(cont>1):
        if(incognita%cont==0):
            cont2+=1
            if(cont2==2):
                return False
        cont-=1
    return True

def main():
    incognita=int(input("digite um numero maior que zero"))
    while incognita>0:
        condicao=primo(incognita)
        print(condicao)
        incognita = int(input("digite um numero maior que zero"))


main()