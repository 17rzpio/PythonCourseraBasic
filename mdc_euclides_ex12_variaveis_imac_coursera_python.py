n = int(input("\ntype positive number go calculate his mdc with euclides algorithm: "))

while n <1:
    n = int(input("\ntype positive number go calculate his value: "))

i = int(input("\ntype positive number go calculate his mdc with euclides algorithm: "))

while i <1:
    i = int(input("\ntype positive number go calculate his value: "))

j = i - n

for k in range(i+1,1,-1):
    if i % k ==0 and j % k ==0:
        print("\nmdc is: ", k)
        break







