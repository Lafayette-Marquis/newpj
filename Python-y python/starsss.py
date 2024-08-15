import turtle

alexa = turtle.Turtle()
alexa.speed(0)
alexa.penup()
alexa.backward(200) 

for i in range(5):
  alexa.pendown()
  for i in range(5):
    alexa.forward(100)
    alexa.right(144)
  alexa.penup()
  alexa.forward(350)
  alexa.right(144)
alexa.pendown()
alexa.left(90)
alexa.forward(150)
alexa.right(90)
alexa.forward(350)
alexa.right(90)
alexa.forward(360)
alexa.right(90)
alexa.forward(350)
alexa.right(90)
alexa.forward(215)
#for i in range(4):
#  alexa.pendown()
#  alexa.forward(350)
#  alexa.left(90)
wn = turtle.Screen()
wn.exitonclick()