def partida():
    vencedor="computador"
    n = int(input("\nQuantas peças?"))
    m = int(input("\nLimite de peças por jogada?"))
    while(n>0 and m>0):
        if((n%(m+1))==0):
            ordem=1
        else:
            ordem=2
        if (ordem == 1):
            print("\nVoce começa!")
            n = n - usuario_escolhe_jogada(n, m)
            if (n <= 0):
                vencedor = "jogador"
                break
            n = n - computador_escolhe_jogada(n, m)
            if (n <= 0):
                vencedor = "computador"
                break
        elif (ordem == 2):
            print("\nComputador começa!")
            n = n - computador_escolhe_jogada(n, m)
            if (n <= 0):
                vencedor = "computador"
                break
            n = n - usuario_escolhe_jogada(n, m)
            if (n <= 0):
                vencedor = "jogador"
                break
    print("\nFim do jogo! O ",vencedor," ganhou!")
def campeonato():
    vencedor="computador"
    rodada=0
    jogadorVit = 0
    computadorVit = 0
    while(rodada<3):
        print("\n**** Rodada ",rodada+1," ****")
        partida()
        if(vencedor=="computador"):
            computadorVit += 1
        else:
            jogadorVit += 1
        rodada+=1
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você ", jogadorVit, " X ", computadorVit, " Computador")

def computador_escolhe_jogada(n,m):
    x=0
    y=0
    while(x<m):
        if(n%(x+1)==0):
            y=x
        x+=1
    if(y<=1):
        y=n-m
    qntdRetira = n-y
    if (n-qntdRetira <= 0):
        return qntdRetira
    print("\nO computador tirou ",qntdRetira," peça.")
    print("\nAgora restam ",n-qntdRetira," peças no tabuleiro.")
    return qntdRetira

def usuario_escolhe_jogada(n,m):
    qntdRetira=int(input("\nQuantas peças você vai tirar?"))
    while(qntdRetira>m or qntdRetira<=0):
        print("\nOops! Jogada inválida! Tende de novo.")
        qntdRetira = int(input("\nQuantas peças você vai tirar?"))
    if (n-qntdRetira <= 0):
        return qntdRetira
    print("\nVocê tirou ",qntdRetira," peça.")
    print("\nAgora resta apenas ",n-qntdRetira," peça no tabuleiro.")
    return qntdRetira

def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    escolha=int(input())
    if(escolha==1):
        print("\nVoce escolheu uma partida isolada")
        partida()
    elif(escolha==2):
        print("\nVoce escolheu um campeonato")
        campeonato()
    else:
        print("\nEscolha entre duas opcoes")
        exit()

