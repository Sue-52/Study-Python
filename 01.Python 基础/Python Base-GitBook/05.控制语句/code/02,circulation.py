# num = 0
# while num<10:
#     num+=1
#     print(num, end="\t")


# num = 0
# sum_all = 0
# sum_even = 0
# sum_odd = 0
# while num <=100:
#     sum_all+=num
#     if(num % 2 ==0):
#         sum_even+=num
#     else:
#         sum_odd+=num
#     num+=1
# print("总数是：{0}，偶数和是：{1}，奇数和是：{2}"123.format(sum_all, sum_even, sum_odd))


# for x in (1,2,3,4,5,6,7):
#     print(x,end="\t")

# for x in range(1,10):
#     sum = ""
#     for y in range(1,x+1):
#         sum+=str.format("{0}*{1}={2}\t",x,y,x*y)
#     print(sum)


# while True:
#     a = input("请输入Q或q")
#     if(a.upper()=="Q"):
#         print("结束")
#         break
#     else:
#         print(a)


# empNum = 0
# salarySum = 0
# salarys = []

# while True:
#     s = input("请输入员工的薪资：（输入Q、q）")
#     if(s.upper()=="Q"):
#         print("ok")
#         break
#     if(float(s)<0):
#         continue
#     empNum+=1
#     salarys.append[float(s)]
#     salarySum += float(s)

# print("员工数{0}".format(empNum))
# print("录入薪资：",salarys)
# print("平均薪资{0}".format(salarySum/empNum))


# names = ("Jason","Eason","Forrest","Sue")
# ages = (20,22,23,21)

# for names,ages in zip(names,ages):
#     print("{0}--{1}".format(names,ages))


# print([x for x in range(0, 10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([x * 2 for x in range(0, 10)])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print([x * 2 for x in range(0, 10) if x % 5 == 0])  # [0, 10]
# print([x for x in "abcde"])  # ['a', 'b', 'c', 'd', 'e']
# cell = [(row,col) for row in range(1,10)for col in range(1,10)]
# print(cell)


# content = "I love JYC before I give up"
# count = {c:content.count(c) for c in content}
# print(count)

# total = {}
# for x in content:
#     total[x]=content.count(x)

# print(total)


# text = {x for x in range(1,100) if x % 8 == 0}
# print(text)  # {32, 64, 96, 8, 40, 72, 16, 48, 80, 24, 56, 88}


gnt = (x for x in range(1,100) if x % 9 == 0)
print(tuple(gnt))  # (9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99)
print(tuple(gnt))  # ()
