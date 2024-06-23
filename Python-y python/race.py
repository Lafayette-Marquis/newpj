import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')

# Create two turtles
bob = turtle.Turtle()
alexa = turtle.Turtle()

# Set turtle shapes
bob.shape("turtle")
alexa.shape("turtle")

# Move turtles to start
bob.penup()
bob.goto(-200, 100)
alexa.penup() 
alexa.goto(-200, -100)

# Countdown
for i in range(3):
  print(3 - i)

# Race
bob.pendown()
alexa.pendown()
bob.forward(random.randint(1, 500))
alexa.forward(random.randint(1, 500))

# Determine winner
if bob.xcor() > alexa.xcor():
  print("Bob won!")
elif alexa.xcor() > bob.xcor():
  print("Alexa won!")  
else:
  print("It's a tie!")
