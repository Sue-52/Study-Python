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
print(del3.remove(100))  # 报错
