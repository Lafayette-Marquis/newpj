#import turtle
#import random
#import string
#def square(x):
#    y = x * x
#    return y
#print(square(4))
#toSquare = 10
#squareResult = square(toSquare)
#print("The square of", toSquare, "is", squareResult)
#assert type (9//5) == int
#assert type (9/5) == float
#def Square(x):
#    runningtotal = 0
#    for counter in range(x):
#        runningtotal = runningtotal + square(counter)
#    return runningtotal
#toSquare = 10
#squareResult = Square(toSquare)
#print("The sum of squares from 0 to", toSquare, "is", squareResult)
#def drawRectangle(t, width, height):
#    for i in range(2):
#        t.forward(width)
#        t.left(90)
#        t.forward(height)
#        t.left(90)
#def drawSquare(t, w):
#  drawRectangle(t, w, w)
#Alexa = turtle.Turtle()
#wn = turtle.Screen()
#drawRectangle(Alexa, 100, 50)
#Alexa.left(90)
#drawRectangle(Alexa, 50, 50)
#wn.exitonclick()