def main():
    n=int(input("digite n "))
    m=int(input("digite m "))
    anterior=n
    atual=m
    resto=atual%anterior
    while resto!=0:
        resto=anterior%atual
        anterior=atual
        atual=resto
    print(f"mdc{n},{m}={anterior}")
main()
