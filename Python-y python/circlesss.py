import math
import turtle

alexa = turtle.Turtle()

def areaOfACircle(radius):
  alexa.circle(radius)
  
  area = math.pi * radius * radius
  return area
areaOfACircle(float(input("What is the radius of the circle? ")))