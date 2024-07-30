x = float(input("\ntype x value than belong graph: "))

while x<0:
    x = float(input("\ntype x value than belong graph: "))
    
y = float(input("\ntype y value than belong graph: "))
while y<0:
    y = float(input("\ntype y value than belong graph: "))

if (x**2 + y**2) >1:
    print("\ndont belong to graph")
else:
    print("\nbelong the graph")
