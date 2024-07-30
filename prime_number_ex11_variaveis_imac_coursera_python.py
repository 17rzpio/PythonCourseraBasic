n = int(input("\ntype positive number go calculate if his value is prime: "))

while n <1:
    n = int(input("\ntype positive number go calculate if his value is prime: "))

count = 0

for k in range(1,n+1):
    if n % k ==0:
        count += 1

if count > 2:
    print("\nnao eh primo")
else:
    print("\nis prime");
        




