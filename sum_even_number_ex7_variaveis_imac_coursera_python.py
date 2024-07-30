n = int(input("\ntype how much number go sum if even in sequence"))

sum_even_number=0

for k in range(n):
    even_number = int(input("\nType the number for sum if is even: "))
    if even_number %2 == 0:
        sum_even_number+=even_number

print("\nsum of even number is: ",sum_even_number)




