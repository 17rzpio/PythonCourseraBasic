n = int(input("\ntype binary number for convert max 10 places: "))

count=0

if n - 1000000000 > 0:
    place1 = n - 1000000000
    placeBit1 = True
else:
    place1 = n
    placeBit1 = False

if place1 - 100000000 > 0:
    place2 = place1 - 100000000
    placeBit2 = True
else:
    place2 = place1
    placeBit2 = False
    
if place2 - 10000000 > 0:
    place3 = place2 - 10000000
    placeBit3 = True
else:
    place3 = place2
    placeBit3 = False

if place3 - 1000000 > 0:
    place4 = place3 - 1000000
    placeBit4 = True
else:
    place4 = place3
    placeBit4 = False

if place4 - 100000 > 0:
    place5 = place4 - 100000
    placeBit5 = True
else:
    place5 = place4
    placeBit5 = False

if place5 - 10000 > 0:
    place6 = place5 - 10000
    placeBit6 = True
else:
    place6 = place5
    placeBit6 = False

if place6 - 1000 > 0:
    place7 = place6 - 1000
    placeBit7 = True
else:
    place7 = place6
    placeBit7 = False

if place7 - 100 > 0:
    place8 = place7 - 100
    placeBit8 = True
else:
    place8 = place7
    placeBit8 = False

if place8 - 10 > 0:
    place9 = place8 - 10
    placeBit9 = True
else:
    place9 = place8
    placeBit9 = False

if place9 - 1 >= 0:
    place10 = 1
    placeBit10 = True
else:
    placeBit10 = False

if placeBit1 == True:
    count+=2**9

if placeBit2 == True:
    count+=2**8
    
if placeBit3 == True:
    count+=2**7

if placeBit4 == True:
    count+=2**6

if placeBit5 == True:
    count+=2**5

if placeBit6 == True:
    count+=2**4   

if placeBit7 == True:
    count+=2**3

if placeBit8 == True:
    count+=2**2

if placeBit9 == True:
    count+=2              

if placeBit10 == True:
    count+=1

print("\nthe binary convert is: ",count+1)

        







