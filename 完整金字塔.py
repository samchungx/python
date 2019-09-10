num = int(input('请输入一个数：'))
print("数字金字塔显示如下：")
level = 1                           #金字塔的高度（金字塔层数）
while level <=num:
    kk=1                        #每一层的长度计数
    t = level
    length = 2*t - 1
    while kk <= length:
        if kk == 1:
            if kk == length:
                print(format(t,str(2*num - 1)+"d"),"\n")
                break
#要形成金字塔，13d 是1的距离，15d是7的距离，然后进行测试
#字要级后的距离比1的距离多2，再减去2倍的层数即可以得到金字塔形状
            else:
                print(format(t,str(2*num + 1 - 2*level)+"d"),"",end='')
                t ==1
        else:
            if kk == length:
                print(t,"\n")
                break
            elif kk <= length/2:
                print(t,"",end="")
                t -= 1
            else:
                print(t,"",end="")
                t += 1
        kk +=1
    level += 1
