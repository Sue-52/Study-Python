# def Person(list):
#     for x in list:
#         try:
#             int(x)
#             print(x)
#         except BaseException as e:
#             print("异常为：{0}".format(e))

# Person([1, "qwe"])

name_file = open("D:/00.study/Study-Python/02.Python 进阶/00.练习/test.txt")
# c = name_file.readline()
num = 0
for x in name_file.read():
    num += 1
    print(x)
# print(c)
print(num)