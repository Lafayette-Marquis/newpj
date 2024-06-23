import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
  
tess = turtle.Turtle() 
tess.shape("turtle")
tess.color("blue")
  
tess.penup()
tess.goto(0, -100)
tess.pendown()
  
tess.pensize(3)
  
# Draw clock face
tess.fillcolor('white')
tess.begin_fill()
tess.circle(100)
tess.end_fill()
  
# Draw numbers
tess.penup()
tess.goto(0, 0) 
tess.setheading(90)
for i in range(-12, 0):
    tess.forward(60)
    tess.pendown()
    tess.write(i - (2 * i))  
    tess.penup()
    tess.goto(0, 0)
    tess.left(30)
      
# Draw hands
# Hour hand
tess.pensize(5)
tess.penup()
tess.goto(0, 0)
tess.setheading(180)
tess.pendown()
tess.forward(50)
  
# Minute hand 
tess.pensize(3)
tess.penup()
tess.goto(0, 0)
tess.setheading(90)
tess.pendown()
tess.forward(70)
  
# Second hand
tess.pensize(2)
tess.penup()
tess.goto(0, 0)
tess.setheading(0)
tess.pendown()
tess.forward(90)

tess.goto(0, 0)
wn = turtle.exitonclick()