n = int(input("type the quantity of sequence: "))
odd_number=[]
for i in range(n):
    number = int(input("type the number of sequence and 0 for end"))
    number2=0                 
    while(number!=0):
        if number%2==0:
            number2+=number
    
        number = int(input("type the number of sequence and 0 for end"))
    odd_number.append(number2)
    number2=0
for i in odd_number:
    print(i)
                     
