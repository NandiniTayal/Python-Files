import turtle

t = turtle.Turtle()

def square(length,angle):
    for i in range(4):
        t.forward(length)
        t.right(angle)

for i in range(24):
    square(100,90)
    t.right(15)
# For faster movement of turtle : t.speed(0)
