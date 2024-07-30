n = int(input("\ntype number go calculate factorial"))

while n < 1:
    n = int(input("\ntype a integer positive number"))

factorial_number=1

for k in range(1,n+1):
    factorial_number*=k

print("\nfactorial number is: ",factorial_number)




