expoente = int(input("\ninsert integer expoente for calcular"))

while expoente <= 0:
    expoente=int(input("\ninsert number integer expoente more than zero: "))

base=int(input("\ninsert base for exponential calculo"))

print("\nthe exponential of ",base,"elevando in ",expoente," is: ")

result_exponential =base

for n in range(expoente-1):
    result_exponential*=base

if expoente==0:
    result_exponential=1

if expoente==1:
    result_exponential = base

print(result_exponential)






