n = int(input("\ntype positive number go calculate fibonacci sequence: "))

while n <1:
    n = int(input("\ntype positive number go calculate his value: "))

count=1
count2=1
print("1")
print("1")
for k in range(n-2):
    count3=count
    count+=count2
    count2=count3
    print(count)

        







