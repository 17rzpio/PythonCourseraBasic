def fatorial(n):
    cont=n
    cont2=cont
    while(cont>2):
        cont2*=(cont-1)
        cont-=1
    return cont2

def main():
    fatorial=int(input("Fatorial de qual numero? "))
    while(fatorial>=0):
        if(fatorial==0 or fatorial==1):
            print(1)
            exit(0)
        n=fatorial(fatorial)
        print(n,end='\t')
        fatorial=int(input("Fatorial de qual numero? "))

main()