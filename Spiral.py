import turtle 

spiral = turtle.Turtle()
spiral.pencolor("blue")
for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()
