# vec = [1,2,3]
# m = 0
# for i in vec:
#     m = m + i
# print(m)
#
# n = 2
# for j in vec:
#     n = n * j
# print(n)


# for i in range(11):
#     while(i>8):
#         print(i*10)
#         break

# for x in range(100):
#     for i in range(2,x):
#         if x%i == 0:
#             j = x/i
#             print('%d 等于 %d * %d' %(x,i,j))
#             break
#         else:
#             print(x,'是一个质数')
#             break


# count = 0
# while count <=5:
#     if count > 3:
#         print(count**2)
#     else:
#         print(count)
#     count = count + 1


# count = 0
# while count < 5:
#     if count > 3:
#         print(count ** 2)
#     else:
#         print(count)
#     count = count + 1          #这个表达式是属于while循环的，不是else的



# evc=[1,3,2,5,8,4,3,4,2,9,8,0]
# for i in range(len(evc)):
#     for j in range(i+1):
#         if evc[i]<evc[j]:
#             tem=evc[i]                 #进行一步转换，Python中不必这么麻烦
            # evc[i]=evc[j]
            # evc[j]=tem
    # print(evc)


#迭代
# d={'a':1,'b':2,'c':3}
# for key in d:
#     print(key)

# for x,y in [(1,1),(2,4),(3,9)]:
#     print(x,y)                    #同时引入两个变量


# for x,y,z in [(1,2,3),(4,5,6),(7,8,9)]:
#     print(x,y,z)                          #同时引入三个变量


# #创建列表解析
# map(lambda x: x**3, range(6))   #计算x的3次幂


# print([x**3 for x in range(6)])       #列表解析

#列表解析嵌套
# print([(i,j) for i in range(3) for j in range(3)])

#增加条件判断语句
# print([(i,j) for i in range(-4,3) if i < 1 for j in range(5) if j > 1])



