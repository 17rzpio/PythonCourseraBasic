n = int(input("\ntype decimal number for convert in binary max 1023: "))

place1 = 0
place2 = 0
place3 = 0
place4 = 0
place5 = 0
place6 = 0
place7 = 0
place8 = 0
place9 = 0
place10 = 0

if n % 2 == 1:
    place1 = 1
n//=2
if n > 1:
    if n % 2 == 1:
        place2 = 1
    n//=2
    if n > 1:
        if n % 2 == 1:
            place3 = 1
        n//=2
        if n > 1:
            if n % 2 == 1:
                place4 = 1
            n//=2
            if n > 1:
                if n % 2 == 1:
                    place5 = 1
                n//=2
                if n > 1:
                    if n % 2 == 1:
                        place6 = 1
                    n//=2
                    if n > 1:
                        if n % 2 == 1:
                            place7 = 1
                        n//=2
                        if n > 1:
                            if n % 2 == 1:
                                place8 = 1
                            n//=2
                            if n > 1:
                                if n % 2 == 1:
                                    place9 = 1
                                n//=2
                                if n > 1:
                                    if n % 2 == 1:
                                        place10 = 1
                            else:
                                if n==1:
                                    place9 = 1
                        else:
                            if n == 1:
                                place8 = 1
                    else:
                        if n == 1:
                            place7 = 1
                else:
                    if n == 1:
                        place6 = 1
            else:
                if n == 1:
                    place5 = 1
        else:
            if n == 1:
                place4 = 1
    else:
        if n ==1:
            place3 = 1
else:
    if n == 1:
        place2=1

print("\nthe decimal in binary convert is: ",place10,place9,place8,place7,place6,place5,place4,place3,place2,place1)

        







