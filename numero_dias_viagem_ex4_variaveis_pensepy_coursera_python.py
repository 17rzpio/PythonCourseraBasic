day_mounth = int(input("\n digite dia do mes"))
day_week = int(input("\ndigite dia da semana em voce ira viajar"))
qntd_day_vacation = int(input("\ndigite quantidade de dias que ficara de ferias"))

qntd_day_vacation2 = qntd_day_vacation % 7 

day_week+=qntd_day_vacation2

qntd_day_vacation%=30
day_mounth+=qntd_day_vacation

print("\no dia da semana que voce voltara eh ",day_week," no dia ",day_mounth)
                 


