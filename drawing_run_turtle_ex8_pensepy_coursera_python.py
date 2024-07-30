import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
count=0
change=0
for n in [1600, -403, 2700, -907, -403, 2000, -9400, 107, -806]:
    alex.forward(100)
    alex.left(n)

wn.exitonclick()

