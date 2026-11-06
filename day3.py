#简易计算器
from random import Random


def calculate(a,b, operation):
    if operation =="+":
       return a+b

    elif operation == "-":
        return a-b
    elif operation == "*":
       return a*b
    elif operation =="/":
        if b== 0:
           return " 除数不能为0 "
        return  a/b
    else:
        return "不支持的运算"

print(calculate(1,4,"*"))

while True:
    user_input=input("input your number/ press q to quit")

    if user_input == "q":
        break
    a=float(user_input)
    operation=input("please input +,-,* /")
    user_input2=input("input your number")
    b=float(user_input2)
    print(calculate(a,b,operation))

#猜数字游戏

from random  import randint
a=randint(1,100)

while True:
    user_input= int(input("guess"))
    if user_input == a:
        break
    elif user_input>a:
        print("too big")
    else:
        print("too small")
    

#
#文件统计器

text= "练习统计里面每个字符出现了多少次，用字典存储并打印结果。提示：用 for 循环遍历字符串的每个字符。"

dic={}

for i in text:
    if i in dic:
       dic[i] += 1

    else:
       dic[i] = 1

print(dic)