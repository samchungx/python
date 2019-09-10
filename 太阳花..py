import turtle
import time
turtle.speed("fastest")
turtle.pensize(5)
turtle.pencolor("red")
for x in range(100):
    turtle.forward(3 * x)
    turtle.left(80)
time.sleep(3)
turtle.done()

