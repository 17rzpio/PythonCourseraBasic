i = int(input("\ntype i positive number go calculate multiple values "))

while i < 1:
    i = int(input("\ntype a integer positive number "))

j = int(input("\ntype j positive number go calculate multiple values "))

while j < 1:
    j = int(input("\ntype a integer positive number "))

n = int(input("\ntype quantity positive number go calculate multiple values "))

while n < 1:
    n = int(input("\ntype a integer positive number "))

multiple_number=[]

count = 0
count2=0

for k in range(n):
    while not(count2 % i == 0 or count2 % j ==0):
        count2+=1
    multiple_number.append(count2)
    count2+=1
    count+=1

for k in range(count):
    print("\nmultiple number is: ",multiple_number[k])




