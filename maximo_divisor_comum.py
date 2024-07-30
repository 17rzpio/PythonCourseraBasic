def main():
    n=int(input("tamanho sequencia"))
    mdc=int(input("primeiro numero sequencia"))
    i=1
    while(i<n):
        print(f"entre com o {i+1} da sequencia")
        numero=int(input())
        i+=1
        divisor=1
        while(divisor<=mdc and divisor <=numero):
            if(mdc%divisor==0 and numero%divisor ==0):
                novo_mdc=divisor
            divisor+=1
        mdc=novo_mdc
    print(f"mdc = {mdc}")
main()
