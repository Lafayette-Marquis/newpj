import turtle

alexa = turtle.Turtle()
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

wn = turtle.Screen()
wn.exitonclick()