n = int(input("\ntype positive number go calculate his is perfect number: "))

while n <1:
    n = int(input("\ntype positive number go calculate his value: "))

count=0

for k in range(n-1,0,-1):
    if n % k ==0:
        count+=k
        if count == n:
           perfect_number = True
        elif count > n:
            perfect_number = False
        else:
            perfect_number = False

if perfect_number==True:
    print("\nperfect number is: ", n)
else:
    print("\ndont is perfect number")
        







