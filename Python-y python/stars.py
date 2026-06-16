import turtle

def draw_star(t):
  for i in range(5):
    t.forward(100)
    t.right(144)

alexa = turtle.Turtle()
wn = turtle.Screen()
for i in range(8):
  draw_star(alexa)
  alexa.right(45)
wn.exitonclick()