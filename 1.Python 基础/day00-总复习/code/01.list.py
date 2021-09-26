# 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），
# 你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；
# 然后，使用 这个列表打印消息，邀请这些人来与你共进晚餐。
# list = ["Sue","Jason","Eason","Richrad","Archor"]
# print(list)

# # 修改嘉宾名单:你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# # 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
# # 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# # 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
# for i in list:
#     if(i == "Eason"):
#         print("Eason can not come to the party")
#     print(i)

# list.insert(0,"Jack")
# list.insert(4,"Allen")
# list.append("Jeff")
# print(
#     list
# )  # ['Jack', 'Sue', 'Jason', 'Eason', 'Allen', 'Richrad', 'Archor', 'Jeff']


# list.pop()
# list.pop()
# list.pop()
# print(list)

# del list[0]
# del list[1]
# print(list)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# 使用一个for 循环打印数字1~20（含）
# for x in range(1,21):
#     print(x)

# 创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）。
# for x in range(1,1000000):
#     # print(x)

# 计 1~1 000 000的总和
# sum = 0
# for x in range(1,1000000):
#     sum+=x
# print(sum)

# 奇数
# for x in range(1,21):
#     if(x % 2 == 1):
#         print(x)

# 3的倍数
# list = []
# for x in range(3,31):
#     if(x % 3 == 0):
#         list.append(x)
# print(list)

# 方立
# list = []
# for x in range(1,11):
#     # print(x**3)
#     list.append(x**3)
# print(list)

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    } 
    
for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + language.title() + ".")

