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
# f = open("file.txt", "a", encoding="utf-8")
# f.truncate(20)
# f.close()

# f = open("file.txt", "r", encoding="utf-8")
# print(f.read())
# sue，---1
# Jason，

# -------------------------------------------------
# 将对象序列化到文件中
# import pickle
# with open(r"file.txt", "wb") as f:
#     name = "Dantes"
#     age = 18
#     arr = [1, 2, 3, 4, 5, 6, 7]

#     pickle.dump(name, f)
#     pickle.dump(age, f)
#     pickle.dump(arr, f)

# -------------------------------------------------
# 将获得到的数据反序列化
# with open(r"file.txt", "rb") as f:
#     a1 = pickle.load(f)
#     a2 = pickle.load(f)
#     a3 = pickle.load(f)
#     print(a1)
#     print(a2)
#     print(a3)

# -------------------------------------------------
# csv 文件的读取
# import csv
# with open(r"xxx.csv", "r") as f:
#     after_read = csv.reader(f)
#     # print(after_read)  # <_csv.reader object at 0x000001B7C5F1DAC8>
#     # print(list(after_read))
#     for x in after_read:
#         print(x)

# csv 文件的写入
# a1 = [5, "jj", 21, "doctor"]
# a2 = [6, "gg", 25, "runner"]
# a3 = [7, "kk", 31, "player"]

# with open(r"xxx.csv", "w") as f:
#     write_csv = csv.writer(f)
#     write_csv.writerow(a1)
#     write_csv.writerow(a2)
#     write_csv.writerow(a3)

# -------------------------------------------------
# os 打开记事本

import os

# os.system("notepad.exe")

# 调用系统的 ping 命令
# os.system("ping www.google.com")
# Pinging www.google.com [157.240.12.35] with 32 bytes of data:
# Request timed out. ...

# os.system("cmd")
# os.system("powershell")

# os.startfile(r"D:/WeChat/WeChat.exe")
