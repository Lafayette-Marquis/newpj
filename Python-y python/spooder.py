import turtle

n = int(input("Enter number of legs: "))
alexa = turtle.Turtle()
wn = turtle.Screen()

angle = input("Enter angle between legs: ")
print(angle)

alexa.speed(0)
for i in range(360):
  alexa.left(1)
  alexa.stamp()
for i in range(n):
  alexa.forward(500)
  alexa.right(45)
  alexa.forward(500)
  alexa.penup()
  alexa.goto(0, 0)
  alexa.pendown()
  alexa.left(float(angle))

alexa.color("blue")
alexa.write(n)
wn.exitonclick()