def main():
    lista=[]
    lista2=[]
    while(True):
        conteudo=int(input("digite um numero ou zero para terminar"))
        if(conteudo!=0):
            lista.append(conteudo)
        else:
            break
    comprimento=len(lista)
    x=comprimento-1
    for i in range(comprimento):
        lista2.append(lista[x])
        x-=1
    for j in lista2:
        print(j)
main()