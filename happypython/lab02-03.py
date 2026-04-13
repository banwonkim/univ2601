#turtle
import turtle

width=int(input('pensize:'))
color=input('color:')

turtle.shape('turtle')
turtle.width(width)
turtle.color(color)

turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)


turtle.pensize(1)
turtle.speed(10)
for j in range(0,10):
    turtle.color('red')
    for i in range(0,100):
        turtle.left(10+i*2)
        turtle.forward(10+i*2)
    turtle.forward(200)

    turtle.color('blue')

    for i in range(100,0,-1):
        turtle.left(10+i*2)
        turtle.forward(10+i*2)
    turtle.forward(200)
