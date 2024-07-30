

print("Calculo de horas pelo relogio")
#print("")

format_hour0=input("digite s se eh formato de 12 em 12 horas em vez de 24 horas")

if(format_hour0=="s"):
    format_hour=input("digite se for formato 12 horas entao se eh am ou pm o formato de hora")

initial_hour=int(input("\ndigite horario inicial"))
interval_hour=int(input("\ndigite o intervalo de horas"))

if(format_hour=="pm"):
   initial_hour+=12
   if(initial_hour==24):
       initial_hour=0
    
if(interval_hour>24):
    interval_hour%=24

if((initial_hour+interval_hour)>24):
    final_hour =(initial_hour+interval_hour)%24
else:
    final_hour = initial_hour+interval_hour

#final_hour = 

print("\n o horario final eh",final_hour)
