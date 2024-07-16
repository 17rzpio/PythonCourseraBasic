# Escreva o seu programa usando o esqueleto sugerido
def fatorialdif(n,m):
    if m==0:
        return 1
    if(m==n):
        return n
    return m*(fatorial(n,m-1))
def fatorial(k):
    if(k==0):
        return 1
    if(k == 1):
        return 1
    return k*(fatorial(k-1))
def potencia(x,e):
    if(e==0):
        return 1
    while(e>1):
        x *= x
        e-=1
    return x
def binomio(n,x,y):
    o=n
    m=0
    b=0
    l=0
    while(n>=0):
        a=potencia(x,n)
        c=potencia(y,b)
        d=fatorial(o)
        e=fatorial(n,l)
        m+=(d/(e*fatorial(l)))*a*c        
        b+=1
        n-=1
        l+=1
    return m
n = float(input("expoente binomio eh "))
x = float(input("digite x"))
y = float(input("digite y"))
print(binomio(n,x,y))

