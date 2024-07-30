a = int(input("\ntype a value of the second degree equation: "))
b = int(input("\ntype b value of the second degree equation: "))
c = int(input("\ntype c value of the second degree equation: "))

delta = b**2-4*a*c
if delta==0:
    root = ((-1)*b)/(2*a)
    print("\nhave just a one root: ",root)
elif delta > 0:
    root1 = ((-1)*b)+(delta**(1/2))/(2*a)
    root2 = ((-1)*b)-(delta**(1/2))/(2*a)
    print("\nhave two root: ",root1,root2)
else:
    real_part = ((-1)*b)/(2*a)
    imaginary_part = (delta*(-1))/(2*a)
    print("\nreal part: ",real_part)
    print("\nimaginary part: ",imaginary_part)
