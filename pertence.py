#-------------------------------------------------
def pertence(item,lista):
    for i in lista:
        if(item==lista):
            return True
    return False
    '''(objeto, list) -> bool

    Recebe uma lista de itens e um item e
    retorna True se o item eh um elemento da lista e
    False em caso contrario.
    '''
    print("Vixe! Ainda nao fiz a funcao!")


#---------------------------------------------------
# testes
lista  = [1, "oi", 3.14, 7, True]

# teste 1
if pertence("oi",lista):
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if pertence(True,lista):
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if not pertence(False,lista):
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

# outros testes

