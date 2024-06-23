import math
import turtle

alexa = turtle.Turtle()

def areaOfACircle(radius):
  alexa.circle(radius)
  
  area = math.pi * radius * radius
  return area
areaOfACircle(100)