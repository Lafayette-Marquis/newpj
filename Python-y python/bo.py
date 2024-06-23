import turtle

def drawSquare(t, sz):
  for i in range(4):
    t.forward(sz)
    t.left(90)
def drawOcto(t):
  for i in range(8):
    t.forward(10)
    t.left(45)
def drawOctoLayerType(t):
    for i in range(13):
        alexa.forward(20)
        alexa.left(45)
    alexa.right(45)
    alexa.left(180)
def newline(t):
  alexa.penup()
  alexa.right(135)
  alexa.forward(15)
  alexa.right(180)
  alexa.forward(495)
  alexa.left(90)
  alexa.forward(45)
  alexa.pendown()
def layer(t):
   for i in range(10):
     drawOctoLayerType(t)

alexa = turtle.Turtle()
drawSquare(alexa, 500)
alexa.forward(10)
drawOcto(alexa)