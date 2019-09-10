while True:
    try:
        num=float(input('请输入一个数字：'))
        if num==0:
            print("输入的数值是零！")
        elif num>0:
            print("输入的数值是正数！")
        elif num<0:
            print("输入的数值是负数！")
        break
    except ValueError:
            print("输入无效，需要重新输入一个数字！")
            
