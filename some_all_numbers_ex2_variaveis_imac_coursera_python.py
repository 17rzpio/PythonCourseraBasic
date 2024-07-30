qntd = int(input("\ninsert quantity of numbers that was some all of him"))

all_number_some=0

for n in range(qntd):
    number_some=int(input("\ninsert number go some"))
    while number_some < 0:
        number_some=int(input("\ninsert number go some more than zero: "))
    all_number_some +=number_some
    
print("\nThe add of all integer numbers positive is: ",all_number_some)   




