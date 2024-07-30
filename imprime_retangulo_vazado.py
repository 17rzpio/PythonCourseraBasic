def main():
    largura=int(input("digite a largura: "))
    altura=int(input("digite a altura: "))
    cont=0
    while(cont<altura):
        cont2=0
        while(cont2<largura):
            if(cont2==0 or cont2==largura-1 or cont==0 or cont==altura-1):
                print("#",end='')
            else:
                print(" ",end='')
            cont2+=1
        print("")
        cont+=1
main()