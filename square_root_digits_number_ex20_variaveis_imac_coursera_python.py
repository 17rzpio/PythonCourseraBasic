print("\ntype number for calculate with four digits: ")

for n in range(1000,9999):
    square_root = n ** (1/2)
    first_ten = int(n / 100)
    second_ten = n - (first_ten*100)
    if (first_ten + second_ten) == square_root:
        print(n)




    


