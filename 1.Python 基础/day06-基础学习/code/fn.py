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

def deepCopy():
    a = [10,20, [5, 6]]
    b = copy.deepcopy(a)
    print("a:", id(a))  # a: 1968601385480
    print("b:", id(b))  # b: 1968601437192
    print("---------------")
    b.append(30)
    b[2].append(7)
    print(a)  # [10, 20, [5, 6]]
    print(b)  # [10, 20, [5, 6, 7], 30]


deepCopy()