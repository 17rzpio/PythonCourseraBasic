a = int(input("\ntype first value of pair: "))
b = int(input("\ntype second value of pair: "))

print(a,b)
every = 0;
count = 0

while(a!=0):
    every+=+1
    term = 1
    for n in range(1,b+1):
        term*=a
    print("Resp = ",term)
    count += term
    print("Sum = ",count)
    a = int(input("\ntype first value of pair: "))
    b = int(input("\ntype second value of pair: "))
    print(a,b)
print("Every pair ",every)
