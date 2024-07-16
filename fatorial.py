# Escreva o seu programa
def fatorial(n,m):
    if(m==n):
        return n
    return m*(fatorial(n,m-1))
n=int(input("digite n"))
m=int(input("digite m"))
print(fatorial(n,m))
