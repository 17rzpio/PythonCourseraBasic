def main():
    largura=int(input("digite a largura: "))
    altura=int(input("digite a altura: "))
    cont=0
    while(cont<altura):
        cont2=0
        while(cont2<largura):
            print("#",end='')
            cont2+=1
        print("")
        cont+=1
main()