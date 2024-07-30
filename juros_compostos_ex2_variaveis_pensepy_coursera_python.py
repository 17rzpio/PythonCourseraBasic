principal_amount=float(input("\ninsert principal ammount ( initial investment)"))
annual_nominal_interest_rate = float(input("\ninsert annual nominal interest rate (as a decimal)"))
number_times_interest_compounded_year = int(input("\ninsert number of times the interest is compounded per year"))
number_year = int(input("\ninsert number of years"))

compound_interest = principal_amount * ((1 + (annual_nominal_interest_rate / number_times_interest_compounded_year))**(number_times_interest_compounded_year * number_year))

print("\nthe value of compound interest: ",compound_interest)
