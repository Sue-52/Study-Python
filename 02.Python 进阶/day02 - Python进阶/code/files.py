# 绝对路径
# file = open(
#     "D:/00.study/Study-Python/02.Python 进阶/day02 - Python进阶/code/file.txt",
#     "a",
#     encoding="utf-8")
# a = "芜湖！！！"
# file.write(a)
# file.close()

# -------------------------------------------------
# 相对路径
# file = open("file.txt", "a", encoding="utf-8")
# a = "芜湖！！！"
# file.write(a)
# file.close()

# -------------------------------------------------
# write 和 writeline
# f = open(r"file.txt", "w", encoding="utf-8")
# s = ["sue\n", "Jason\n", "Eason\n", "Forrest\n"]
# f.writelines(s)
# f.close()

# -------------------------------------------------
# 使用 try...except... 确保关闭：
# try:
#     file = open(r"file.txt", "a", encoding="utf-8")
#     str = "Sue,大帅逼！！！\n"
#     file.write(str)
# except BaseException as e:
#     print(e)
# finally:
#     file.close()

# -------------------------------------------------
# 使用 with 语句确保关闭:
# arr = ["primary\n", "middle\n", "high\n"]
# with open(r"file.txt", "a", encoding="utf-8") as file:
#     file.writelines(arr)

# -------------------------------------------------
# read() 读取方法
# with open(r"file.txt", "r", encoding="utf-8") as f:
#     print(f.read(10))

# -------------------------------------------------
# readline() 读取方法
# with open(r"file.txt", "r", encoding="utf-8") as f:
#     print(f.readline())  # sue，Jason，Eason，Forrest，primary，middle，high

# -------------------------------------------------
# readlines() 读取方法
# with open(r"file.txt", "r", encoding="utf-8") as f:
#     print(f.readlines())
#     # ['sue，Jason，\n', 'Eason，Forrest，\n', 'primary，middle，\n', 'high\n']

# # 练习
# with open(r"file.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(lines)
#     lines = [
#         line.strip() + "---" + str(index + 1) + "\n"
#         for index, line in enumerate(lines)
#     ]
#     print(lines)

# with open(r"file.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# -------------------------------------------------
# 二进制文件操作
# with open(r"cat.gif", "rb") as f:  # 要拷贝的二进制文件
#     with open(r"copy_one.gif", "wb") as w:  # 拷贝后的二进制文件
#         for line in f.readlines():
#             w.write(line)
# print("拷贝结束")

# -------------------------------------------------
# 练习 truncate、seek、flush 方法
# with open(r"file.txt", "r", encoding="utf-8") as f:
#     f.seek(2)  # 索引 --- 指针
#     print(f.read())
#     # ，---1
#     # Jason，---2
#     # Eason，---3
#     # Forrest，---4
#     # primary，---5
#     # middle，---6
#     # high，---7
#     print(f.name)  # file.txt
#     print(f.mode)  # r
#     print(f.closed)  # False
# print(f.closed)  # True

# -------------------------------------------------
# file = open(r"file.txt", "r", encoding="utf-8")
# file.flush()  # write也并不是直接写入，也会将数据放入缓冲区中
# file.close()

# -------------------------------------------------
f = open("file.txt", "a", encoding="utf-8")
f.truncate(20)
f.close()

f = open("file.txt", "r", encoding="utf-8")
print(f.read())
# sue，---1
# Jason，