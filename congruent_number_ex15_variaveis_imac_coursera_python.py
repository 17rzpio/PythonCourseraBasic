n = int(input("\ntype quantity first positive number go calculate congruent number: "))

while n <1:
    n = int(input("\ntype positive number go calculate his value: "))

j = int(input("\ntype second positive number go calculate congruent number: "))

while j <1:
    j = int(input("\ntype positive number go calculate his value: "))

m = int(input("\ntype module positive number go calculate congruent number: "))

while m <1:
    m = int(input("\ntype positive number go calculate his value: "))

for k in range(n):
    if k % m == j %m:
        print("\nj is ",j," is congruent number: ",k)
        







