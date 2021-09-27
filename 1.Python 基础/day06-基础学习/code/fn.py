# def addNum():
#   print("函数测试")
# addNum()

# def compMax(a,b):
#     if(a<b):
#         print(b,"--b--打")
#     else:
#         print(a,"--a--打")

# compMax(1, 21)  #2 1 --b--打
# compMax(19, 8)  # 19 --a--打




# def test():
#   """测试注释"""
#   print("Hello Function")
# test()
# help(test.__doc__)




# def fnAdd(a,b):
#     return a+b

# c = fnAdd(1,5)
# print(c)  # 6
# print(fnAdd)  # <function fnAdd at 0x0000022B30DCD8B8>
# print(id(fnAdd))  # 2115667351736




# a = 100
# def f1():
#     a = 200
#     print(a)
#     print(globals())



# f1()
# print(a)

# import math
# import time

# def test01():
#     start = time.time()
#     for i in range(1000000):
#         math.sqrt(30)
#     end = time.time()
#     print("耗时：{0}".format((end-start)))

# def test02():
#     b = math.sqrt
#     start = time.time()
#     for i in range(1000000):
#         b(30)
#     end = time.time()
#     print("耗时：{0}".format((end-start)))

# test01()  # 耗时：0.1767582893371582
# test02()  # 耗时：0.14059734344482422



# a = [1,2,3,4,5]

# def fn01(b):
#     print(id(b))
#     a.append(6) #
#     print(id(b))

# fn01(a)
# print(id(a))
# print(a)



# a = 100
# def fn01(b):
#     print("b:", id(b))  # b: 140732072099168
#     b += 100
#     print("b:", id(b))  # b: 140732072102368
#     print(b)  # 200

# fn01(a)
# print("a:", id(a))  # a: 140732072099168




import copy

# a = [1,2,3,[4,5]]
# b = copy.copy(a)
# print("a:", id(a))  # a: 2261211812168
# print("b:", id(b))  # b: 2261211769160
# print("---------------")
# b.append(6)
# b[3].append(10)
# print(a)  # [1, 2, 3, [4, 5, 10]]
# print(b)  # [1, 2, 3, [4, 5, 10], 6]

# def deepCopy():
#     a = [10,20, [5, 6]]
#     b = copy.deepcopy(a)
#     print("a:", id(a))  # a: 1968601385480
#     print("b:", id(b))  # b: 1968601437192
#     print("---------------")
#     b.append(30)
#     b[2].append(7)
#     print(a)  # [10, 20, [5, 6]]
#     print(b)  # [10, 20, [5, 6, 7], 30]

# deepCopy()

# def fn01(a,b,c):
#     return a+b+c

# print(fn01(1,2,3))
# print(fn01(1,3))




# def fn01(a,b,c,d=10,e=11):
#     return a+b+c+d+e

# print(fn01(1,2,3))
# print(fn01(1,3))



# def fn01(a, b, c):
#     print(a,b,c)
#     return a + b + c

# print(fn01(1, 2, 3)) # 位置参数
# print(fn01(b=20,c= 12,a=13)) # 命名参数


# def fn01(a,b,*c):
#     print(a,b,c)

# fn01(8,9,19,20)

# def fn02(a,b,**c):
#     print(a,b,c)

# fn02(8,9,name="sue",age=18)

# def fn03(a,b,*c,**d):
#     print(a,b,c,d)

# fn03(8,9,20,12,"sue",name="sue",age=18,flag=True)



# def fn01(*a,b,c):
#     print(a,b,c)
# # fn01(2,3,4) # 报错，由于 a 是可变参数，将2，3，4全部手机。造成了 b 和 c 没有赋值
# fn01(2, 3, 4, b=13, c=10)  # (2, 3, 4) 13 10



# fn = lambda a,b,c:a+b+c
# print(fn)  # <function <lambda> at 0x000002465AC3E8B8>
# print(fn(1, 2, 3))  # 6

# g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
# print(
#     g
# )  # [<function <lambda> at 0x000001FB6F06EA68>, <function <lambda> at 0x000001FB6F06EAF8>, <function <lambda> at 0x000001FB6F06EB88>]
# print(g[0](6), g[1](7), g[2](8))  # 12 21 32



# eval("print('Hello')")  # Hello
# a = 10
# b = 20
# c = eval("a+b")
# print(c)  # 30

# dict01 = dict(a=100,b=200)
# d = eval("a+b",dict01)
# print(d)  # 300



# def factorial(n):
#     if n == 1: return 1
#     return n*factorial(n-1)
# for x in range(1,6):
#     print(x,"!=",factorial(x))



# def fn01():
#     print("running...01")

#     def fn02():
#         print("running...02")
#     fn02()
# fn01()



# def get_name(isChinese,name,familyName):
#     def print_name(a,b):
#         print("{0} {1}".format(a,b))

#     if isChinese:
#         print_name(familyName,name)
#     else:
#         print_name(name,familyName)

# get_name(True,"傲","苏")
# get_name(False,"Edmond","Dantes")



# def outer():
#     a = 100
#     def inner():
#         nonlocal a
#         print("inner a: {0}".format(a))
#         a = 200
#     inner()
#     print("outer a: {0}".format(a))
# outer()



# 自定义的方法 -- 引入的方法名必须和文件名一样
# import gointo as money

# money.make_money(300)