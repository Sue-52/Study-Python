# list = list()  # []
# list = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = list("full stack")  # ['f', 'u', 'l', 'l', ' ', 's', 't', 'a', 'c', 'k']
# print(list)

# num1 = list(range(3, 15, 2))
# num2 = list(range(15, 20, 2))
# num3 = list(range(15, 3, -2))
# num4 = list(range(20, 15, -1))
# print(num1)  # [3, 5, 7, 9, 11, 13]
# print(num2)  # [15, 17, 19]
# print(num3)  # [15, 13, 11, 9, 7, 5]
# print(num4)  # [20, 19, 18, 17, 16]

# a1 = [x * 2 for x in range(5)]
# a2 = [x * 2 for x in range(100) if x % 9 == 0]
# print(a1)  # [0, 2, 4, 6, 8]
# print(a2)  # [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]

add1 = [1, 2, 3]
add1.append(4)
print(add1)

add2 = [1, 2, 3, 4]
add2 = add2 + [5]  # [1, 2, 3, 4, 5]
print(add2)

add3 = [5, 6, 7]
add3.extend([1, 2, 3])  # [5, 6, 7, 1, 2, 3]
print(add3)

add4 = [1, 2, 3, 4]
add4.insert(2, 100)
print(add4)  # [1, 2, 100, 3, 4]

del1 = [10, 20, 30, 40, 50]
del del1[1]
print(del1)  # [10, 30, 40, 50]

del2 = [10, 20, 30, 40, 50, 60]
a = del2.pop()
print(del2, a)  # [10, 20, 30, 40, 50]
b = del2.pop(0)
print(del2, b)  # [20, 30, 40, 50]

del3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
del3.remove(0)
print(del3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(del3.remove(100))  # 报错

visit1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(visit1[0])  # 1

visit2 = ["sss", "a", "b", "c"]
print(visit2.index("sss"))  # 0
print(visit2.index("b", 2))  # 2

total1 = [1, 1, 2, 23, 43, 5, 6576, 65, 5, 5, 7, 98, 9]
# print(total1.count(1))  # 2
print(len(total1))

total1 = [11, 2, 2, 3, 44, 55, 66, 77, 88]
print(20 in total1)  # False
print(44 in total1)  # True

# 提取整个列表
s = [10, 20, 30, 40, 50, 60, 70]
print(s[:])  # [10, 20, 30, 40, 50, 60, 70]

# [start:] 从 start 索引开始到结尾
print(s[1:])  # [20, 30, 40, 50, 60, 70]

# [:end] 从头开始直到 end-1
print(s[:4])  # [10, 20, 30, 40]

# [start:end] 从 start 到 end-1
print(s[0:5])  # [10, 20, 30, 40, 50]

# [start:end:step] 从 start 提取到 end-1，步长为step
print(s[1:6:2])  # [20, 40, 60]

y = [10, 20, 30, 40, 50, 60, 70]

# 倒数三位数
print(y[-3:])  # [50, 60, 70]

# 倒数第五到倒数第三
print(y[-5:-3])  # [30, 40]

# 步长为负，从右到左依次提取
print(y[::-1])  # [70, 60, 50, 40, 30, 20, 10]

lie1 = [100, 20, 32, 543, 32, 1, 0]
# 升序
lie1.sort()
print(lie1)  # [0, 1, 20, 32, 32, 100, 543]
# 降序
lie1.sort(reverse=True)
print(lie1)  # [543, 100, 32, 32, 20, 1, 0]
# 打乱顺序
import random

# 每次执行结果都是随机的
random.shuffle(lie1)
print(lie1)  # [0, 543, 100, 20, 32, 1, 32]

lie2 = [100, 23, 432, 54, 213, 76, 0, 4, 66, 76]
# 升序
lie3 = sorted(lie2)
print(lie3)  # [0, 4, 23, 54, 66, 76, 76, 100, 213, 432]
# 降序
lie3 = sorted(lie2, reverse=True)
print(lie3)  # [432, 213, 100, 76, 76, 66, 54, 23, 4, 0]

lie4 = [20, 10, 30, 50, 40]
lie5 = reversed(lie4)
print(lie5)  # <list_reverseiterator object at 0x00000184C1E20508>
# 通过lise进行转换
print(list(lie5))  # [40, 50, 30, 10, 20]
# 第二次即为空
print(list(lie5))  # []

lie6 = [10, 40, 90, 30, 44, 70]
print(max(lie6))  # 90
print(min(lie6))  # 10

lie7 = [1, 6, 2, 4, 9, 4, 4, 87]
print(sum(lie7))  # 117

info = [
  ["高小一",18,30000,"北京"],
  ["高小2",19,20000,"上海"],
  ["高小5",20,10000,"深圳"],
]
print(info)
print(info[0][1])  # 18
