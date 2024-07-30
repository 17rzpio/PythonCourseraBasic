n = int(input("type the n of hypotenuse: "))

for m in range(n):
    for i in range(m):
        for j in range(m):
            if ((m**2)==(i**2)+(j**2)):
                print(m)
