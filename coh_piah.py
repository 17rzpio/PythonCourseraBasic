import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    return (abs(as_a[0]-as_b[0])+abs(as_a[1]-as_b[1])+abs(as_a[2]-as_b[2])+abs(as_a[3]-as_b[3])+abs(as_a[4]-as_b[4])+abs(as_a[5]-as_b[5]))/6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #wal_lista_texto = []
    #ttr_lista_texto = []
    #hlr_lista_texto = []
    #sal_lista_texto=[]
    lista_tamanhos=[]
    palavras_diferentes=[]
    sentencas=separa_sentencas(texto)
    cont11=0
    for i in sentencas:
        cont11+=len(i)
    cont5 = len(sentencas)
    #cont4=0
    cont = 0
    cont6=0
    cont7=0
    cont3=0
    cont8 = 0
    cont4 = 0
    cont9 = 0
    cont12=0
    lista_total_palavras=[]
    for m in sentencas:


        frases=separa_frases(m)
        cont8+=len(frases)

        for p in frases:
            palavras=separa_palavras(p)
            cont12+=len(p)
            cont2=palavras[0]
            cont3+=len(palavras)

            cont6+=len(palavras)
            unico=True
            unico2=True

            for q in palavras:
                lista_total_palavras.append(q)

                tamanho=len(q)
                cont+=tamanho


                cont4+=tamanho



            cont7+=len(palavras)


    cont9=n_palavras_diferentes(lista_total_palavras)
    cont10=n_palavras_unicas(lista_total_palavras)

    pal=cont12/cont8
    sac = cont8 / cont5

    sal = (cont11) / cont5



    wal_lista_texto=cont4/cont6
    ttr_lista_texto=cont9/cont6
    hlr_lista_texto=cont10/cont6
    sal_lista_texto=sal


    return [wal_lista_texto, ttr_lista_texto, hlr_lista_texto, sal_lista_texto, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    cont3=1
    cont2=1
    primeira_assinatura=calcula_assinatura(textos[0])
    cont=compara_assinatura(primeira_assinatura,ass_cp)
    for m in textos:
        assinatura=calcula_assinatura(m)
        s=compara_assinatura(assinatura,ass_cp)
        if(s<cont):
            cont=s
            cont3=cont2
        cont2+=1
    return cont3