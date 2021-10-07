# -----------------------等边三角形--------------------------
num = input("请用户输入一个数字：")
n = int(num)
# # 通过给定的层数做循环
# for i in range(1, n):
#     # 这层循环由于遍历的三角右侧的空格有多少
#     for j in range(1, n - i):
#         print(end=" ")
#     # 这层循环由于输出星号，在上面的循环结束后，在其后的位置添加 *
#     for k in range(n - i, n):
#         print("*", end=" ")
#     # 用于换行
#     print("")

# -----------------------直角三角形--------------------------
# for i in range(1, n):
#     for j in range(0, i):
#         print("*", end=" ")

#     print("")

# -----------------------倒直角三角形--------------------------
# for i in range(1, n):
#     for j in range(i, n):
#         print("*", end=" ")

#     print("")

# -----------------------反直角三角形--------------------------
# for i in range(1, n):
#     for j in range(0, n - i):
#         print(" ", end=" ")
#     for k in range(n - i, n):
#         print("*", end=" ")

#     print("")

# -----------------------倒反直角三角形--------------------------
# for i in range(1, n):
#     for j in range(1, i):
#         print(" ", end=" ")

#     for j in range(i, n):
#         print("*", end=" ")

#     print("")
