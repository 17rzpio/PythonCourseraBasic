n = int(input("type the n: "))

m = int(input("type the m: "))
count=0
for x in range(m):
    for y in range(n):
        if(x*y-x**2+y)>count:
            count = (x*y-x**2+y)
            max_x=x
            max_y=y

print("max value: ",count," x ",max_x," y ",max_y)
