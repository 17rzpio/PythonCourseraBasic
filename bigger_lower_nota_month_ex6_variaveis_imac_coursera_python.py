n = int(input("\ntype how much denshi in the class of mac introduction to automatos of stack"))

nota_first_avaliation = []

nota_less = 100

nota_full = 0

for k in range(n):
    nota = 0
    nota = int(input("\ntype the note"))
    while nota <0 and nota > 100:
        nota = int(input("\ntype the note minimo 0 and max is 100"))
    if nota > nota_full:
                         nota_full = nota
    if nota < nota_less:
                         nota_less = nota
    nota_first_avaliation.append(nota)

print("bigger nota is: ",nota_full," and less nota is: ",nota_less)




