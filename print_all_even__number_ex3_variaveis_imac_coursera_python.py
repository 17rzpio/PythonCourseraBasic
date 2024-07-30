limit_even = int(input("\ninsert quantity of numbers that was print even all of him"))

while limit_even <= 0:
    limit_even=int(input("\ninsert number go some more than zero: "))

print("\nthe sequence of even number is: ")


for n in range(limit_even+1):
    if n%2!=0:
        print(n)






