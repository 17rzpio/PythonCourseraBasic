a = int(input("\ntype first side for calculate rectangle triangle: "))

b = int(input("\ntype second side for calculate rectangle triangle: "))

c = int(input("\ntype third side for calculate rectangle triangle: "))

if a > b and a > c:
    if a**2 >= b**2+c**2:
        print("\nare sides of triangle")
    else:
        print("\nnot are sides of triangle")
elif b > a and b > c:
    if b**2 >= a**2 + c**2:
        print("\nare sides of triangle")
    else:
        print("\nnot are sides of triangle")
elif c > a and c > b:
    if c**2 >= a**2 + b**2:
        print("\nare sides of triangle")
    else:
        print("\nnot are sides of triangle")
else:
    print("\nnot are sides of triangle")
    


