expression=input("\nescolha qual calculo, 1 ou 2")
value1=int(input("\ndigite primeiro valor"))
value2=int(input("\ndigite primeiro valor"))
value3=int(input("\ndigite primeiro valor"))
if(expression=="1"):
    result = value1 * value2 - value3
else:
    result = value1 * (value2 - value3)
print("resultado",result)

    
