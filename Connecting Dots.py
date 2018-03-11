import turtle 

dots = turtle.Turtle()
dot_dist = 25
width=7
height=7
dots.penup()
dots.left(90)
dots.forward(150)
dots.right(90)
for i in range(height):
    for j in range(width):
         dots.dot()
         dots.forward(dot_dist)
    dots.backward(width*dot_dist)
    dots.right(90)
    dots.forward(dot_dist)
    dots.left(90)
turtle.done()
