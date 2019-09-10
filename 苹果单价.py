# coding:utf-8
applePricestr="Apple's unit price is 8 yuan"
applePricestr=applePricestr[22]
print('提取苹果的单价：'\
     ,applePricestr,\
        ',此刻他的数据类行为：'\
    ,type(applePricestr))
applePricestr=str(applePricestr)
print('转型数据类型后:',type(applePricestr))



