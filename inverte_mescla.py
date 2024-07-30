def main():
    # escreva o seu programa abaixo e remova o print()
    print("Vixe! Ainda nao fiz o exercicio!")
    lista1=[5,6,7]
    lista2=[5,8,9]
    lista3=mesclar(lista1,lista2)
    for n in lista3:
        print(n)
def mesclar(lista2,lista3):
    lista1=lista2+lista3
    lista1.sort()
    x=lista1[:]
    lista2=[]
    for n in range(len(lista1)):
        if(n==(len(lista1))-1):
            if(x[n]==x[n-1]):
                break
            else:
                lista2.append(lista1[n])
                break
        if not (x[n+1]==lista1[n]):
            lista2.append(lista1[n])
    lista2.sort()
    return lista2
main()
