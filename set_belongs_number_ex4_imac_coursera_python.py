n = int(input("\ntype n value of the sequence: "))
count=0
for m in range(n):
    x= float(input("\ntype the x for the value of the sequence"))
    y= float(input("\ntype the x for the value of the sequence"))
    if (x<=0) and (y<0) and (y+x**2+2*x-3 <=0):
        if (x>=0) and (y+x**2-2*x-3 <=0):
            count+=1
print("\ntotal of points belong the set: ",count)
