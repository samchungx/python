import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
turtle.pencolor("green")
for x in range(300):
    turtle.forward(2 * x)
    turtle.left(90)
time.sleep(3)
turtle.done()

