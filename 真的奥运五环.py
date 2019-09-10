#奥运五环绘制
from turtle import *
seth(90)
speed(5)                   #设置速度
pensize(10)                 #设置尺寸
pencolor("blue")            #设置颜色
circle(50)                  #设置圆的半径，往下统一用50

penup()
right(90)
forward(75)                 #移动到黑环
pendown()
left(90)
pencolor("black")
circle(50)
penup()
right(90)
forward(75)                 #移动到红环的位置
pendown()
left(90)
pencolor("red")
circle(50)

penup()
goto(35,-50)                #移动到黄环的位置
pendown()
pencolor("yellow")
circle(50)
penup()
goto(115,-50)               #移动到绿环的位置
pendown()
pencolor("green")
circle(50)

hide()                      #隐藏图标
done()
