n = int(input("type the n: "))

count=0
for m in range(1,n+1):
    for k in range(1,m+1):
        if (k%n==0):
            count+=1
    if count<=2:
        prime_sum+= m
print(prime_sum)
