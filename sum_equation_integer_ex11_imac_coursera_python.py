n = int(input("\ntype n value for equation: "))
solution_set=0
for i in range(1,n+1):
    solution_set += (i/(n-i+1))
print(solution_set)
    




