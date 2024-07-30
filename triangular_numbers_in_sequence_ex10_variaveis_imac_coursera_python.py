i = int(input("\ntype number go calculate if his value is triangular calculate "))

count = 0
count2=0
count3=0

triangular_number = False

for n in range(i):
    for k in range (i):
        for j in range(i):
            if count * count2 * count3 == i:
                if count > count2 and count > count3 and count2 > count3:
                    if count3 + 1 == count2 and count2 + 1 == count:
                        triangular_number = True
                if count > count3 and count > count2 and count3 > count2:
                    if count2 + 1 == count3 and count3 + 1 == count:
                        triangular_number = True
                if count3 > count and count3 > count2 and count > count2:
                    if count2 + 1 == count and count + 1 == count3:
                        triangular_number = True
                if count3 > count and count3 > count2 and count2 > count:
                    if count + 1 == count2 and count2 + 1 == count3:
                        triangular_number = True
                if count2 > count and count2 > count3 and count > count3:
                    if count3 + 1 == count and count + 1 == count2:
                        triangular_number = True
                if count2 > count and count2 > count3 and count3 > count:
                    if count + 1 == count3 and count3 + 1 == count2:
                        triangular_number = True                
            count3+=1
        count3=0
        count2+=1
    count2=0
    count+=1

print("\nThis number boolean if is triangular number calculate is: ",triangular_number)






