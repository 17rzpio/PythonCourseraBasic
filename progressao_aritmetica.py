def teste():
# Escreva o seu programa
    n=int(input("digite qnts termos"))
    cont2=0
    while(cont2<n):
        cont=int(input("digite termo"))
        if(cont2==0):
            primeiro=cont
        if(cont2==1):
            segundo=cont
        if(cont2==2):
            terceiro=cont
            if(segundo!=((primeiro+terceiro)/2)):
               return False
        if(cont2>2):
            primeiro=segundo
            segundo=terceiro
            terceiro=cont
            if(segundo!=((primeiro+terceiro)/2)):
               return False
        cont2+=1
    return True
#-------------------------------------------------
resultado=teste()
print(resultado)
