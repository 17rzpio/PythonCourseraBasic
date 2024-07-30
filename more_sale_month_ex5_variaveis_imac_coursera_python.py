qntd_sale_disc = []

before_day_sale=0

day_most_sale=0

for n in range(31):
    print("\nDay: ",n+1)
    disc_sale_in_a_day = int(input("\nInsert quantity of disc sale in that day: "))
    qntd_sale_disc.append(disc_sale_in_a_day)
    if disc_sale_in_a_day > before_day_sale:
        before_day_sale = disc_sale_in_a_day
        day_most_sale = n+1

print("The day than most disc sale is: ",day_most_sale," and the quantity is: ",before_day_sale)





