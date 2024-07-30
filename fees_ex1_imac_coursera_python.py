x = float(input("\ntype capital value of complex fee: "))
z = float(input("\ntype how much fee monthly are in one year: "))
amount=x
for n in range(1,13):
    amount = amount*(1+z)
    print("\nthe month ",n,"have amount of fee: ",amount)
