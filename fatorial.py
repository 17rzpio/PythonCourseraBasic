def main():
    fatorial=int(input("Fatorial de qual numero? "))
    if(fatorial==0 or fatorial==1):
        print(1)
        exit(0)
    cont=fatorial
    cont2=cont
    while(cont>2):



        cont2*=(cont-1)

        cont-=1
    print(cont2,end='\t')
main()