numbers_integer=[]
numbers_integer.append(int(input("insert integer numbers sequence seguida of zero")))
cont=0
while numbers_integer[cont]!=0:
    cont+=1
    numbers_integer.append(int(input("insert integer numbers sequence seguida of zero")))
for n in numbers_integer:
    square=n**2
    print("\nsquare of integer number",n," is: ",square)


