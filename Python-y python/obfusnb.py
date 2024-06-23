import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alexa = turtle.Turtle()
alexa.speed(0)
drawSquare(alexa, 100)

alexa.penup()
alexa.goto(0,0)
alexa.pendown()

drawSquare(alexa, 50)
size = 20
for i in range(70):
    drawSquare(alexa, size)
    size += 10
    alexa.forward(10)
    alexa.right(18)
wn.exitonclick()