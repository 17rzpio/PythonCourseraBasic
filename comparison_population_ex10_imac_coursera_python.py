n = int(input("\ntype n value of citizens city one: "))
k = int(input("\ntype second population: "))
x = float(input("\ntype rate of grow up in city one: "))
y=float(input("\ntype rate of grow up in second city: "))
if x>y:
    if n>k:
        print("\nthe second city never go grow up more than second")
    else:
        print("\nthe first city go grow up and surpass the second")
else:
    if n>k:
        print("\n the second city go surpass the first")
    else:
        print("\nthe second city ever go be bigger")



