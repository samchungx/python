import turtle
def drawSnake(rad,angle,len,neckrad):   #rad描述圆形轨迹半径的位置，angle表示小乌龟沿着圆形爬行的弧度制
    for i in range(len):
        turtle.circle(rad,angle)        #让小乌龟沿着一个圆形爬行
        turtle.circle(-rad,angle)
        turtle.circle(rad,angle/2)
        turtle.fd(rad)                  #表示小乌龟向前沿直线爬行移动，参数表示爬行的距离
        turtle.circle(neckrad+1,180)
        turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)      #该函数用于启动一个图形窗口
    #参数：启动窗口宽度为1300像素、高度为800,（0,0）表示窗口左上角在屏幕中的坐标位置
pythonsize = 30
    turtle.pensize(pythonsize)      #运动轨迹的宽度
    turtle.pencolor("blue")         #运动轨迹的颜色
    turtle.seth(-40)                #启动时运动的方向，负值表示相反方向；表示向东南方向40度
    drawSnake(40,80,5,pythonsize/2)
​main()      #main()函数给出了轨迹窗体的大小，爬行轨迹的颜色和宽度以及初始爬行方位