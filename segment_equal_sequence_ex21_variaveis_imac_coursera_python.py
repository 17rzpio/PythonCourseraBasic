n = int(input("\ntype number for quantity of sequence: "))

sequence = []

count2 = 0

input_type = int(input("\ntype the numbers of sequence"))
sequence.append(input_type)
count = input_type

for k in range(1,n):
    input_type = int(input("\ntype the numbers of sequence"))
    sequence.append(input_type)
    if input_type == count:
        count2+=1
    count = input_type

print("\nthe number of consecutive numbers in sequence is: ",count2)






    


