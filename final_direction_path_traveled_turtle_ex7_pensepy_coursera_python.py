import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
count=0
change=0
for n in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.left(n)
    angle=n
    if n<(-360):
        angle = n%360
    if angle<0:
        angle=360-angle
    if angle>90:
        change+=angle//90
    count=0
wn.exitonclick()
if change//4==1 or change//4==5:
    print("left")
elif change//4==2 or change//4==6:
    print("back")
elif change//4==3 or change//4==7:
    print("right")
elif change//4==0 or change//4==4:
    print("same");
