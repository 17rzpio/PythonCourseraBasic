import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for n in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.left(n)

wn.exitonclick()
