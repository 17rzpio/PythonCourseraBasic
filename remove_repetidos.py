def remove_repetidos(lista):
    lista.sort()
    x=lista[:]
    lista2=[]
    for n in range(len(lista)):
        if(n==(len(lista))-1):
            if(x[n]==x[n-1]):
                break
            else:
                lista2.append(lista[n])
                break
        if not (x[n+1]==lista[n]):
            lista2.append(lista[n])
    return sorted(lista2)
