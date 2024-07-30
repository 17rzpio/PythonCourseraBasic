def main():
    m=int(input("digite m"))
    for n in range(m):
        soma=0
        inicio=1
        while(soma!=n*n*n):
            soma=0
            for i in range(n):
                
                soma=soma+inicio+2*i
            inicio+=2
        inicio-=2
        print(f"{n}*{n}*{n} = {inicio}")
        for i in range(1,n):
            print(f"+{inicio+2*i}")
        print()
main()
