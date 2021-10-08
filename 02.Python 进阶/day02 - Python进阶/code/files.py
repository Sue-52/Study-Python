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

# from genericpath import getatime
# import os

# os.system("notepad.exe")

# 调用系统的 ping 命令
# os.system("ping www.google.com")
# Pinging www.google.com [157.240.12.35] with 32 bytes of data:
# Request timed out. ...

# os.system("cmd")
# os.system("powershell")

# os 模块文件操作
# os.startfile(r"D:/WeChat/WeChat.exe")
# os.rename("./cat.gif", "rename_cat.gif")
# os.remove("./file1.txt")
# file_pro = os.stat("file.txt")
# print(
#     file_pro
# )  # os.stat_result(st_mode=33206, st_ino=3659174697668209, st_dev=1986293374, st_nlink=1, st_uid=0, st_gid=0, st_size=43, st_atime=1633682811, st_mtime=1633607574, st_ctime=1633508935)

# file_list = os.listdir("D:/00.study/")
# print(file_list)

# os文件目录操作
# os.mkdir("works")
# os.makedirs("works/jobs/stu") ,
# os.rmdir("works")
# os.removedirs("works/jobs/stu")
# os.getcwd()
# os.chdir("xxx")
# os.walk()
# print(os.name)  # nt --> windows; linux&unix -->posix

# -------------------------------------------------
# os.path 模块目录操作
# print(os.path.isabs("file.txt"))  # False
# print(os.path.isdir("file.txt"))  # False
# print(os.path.isfile("file.txt"))  # True
# print(os.path.exists("file.txt"))  # True
# print(os.path.getsize("file.txt"))  # 43
# print(os.path.abspath("file.txt"))
# # D:\00.study\Study-Python\02.Python 进阶\day02 - Python进阶\code\file.txt
# print(os.path.dirname(__file__))
# # d:\00.study\Study-Python\02.Python 进阶\day02 - Python进阶\code
# print(os.path.getatime("file.txt"))  # 1633682811.951791
# print(os.path.getmtime("file.txt"))  # 1633607574.351463
# # print(os.path.join())
# print(os.path.split("file.txt"))  # ('', 'file.txt')
# print(os.path.splitext("file.txt"))  # ('file', '.txt')

# -------------------------------------------------
# walk方法的使用：
# os.makedirs("works/some/www")
# path = os.getcwd()
# # print(path)
# file_lists = os.walk(path)
# # print(list(file_lists))
# for dirpaths, dirnames, filenames in file_lists:
#     # print(dirpaths)
#     # print(dirnames)
#     # print(filenames)
#     for dirP in dirnames:
#         # print(dirP)
#         print(os.path.join(dirpaths, dirP))

#     for names in filenames:
#         print(os.path.join(dirpaths, names))

# -------------------------------------------------
# shutil 模块的使用
import shutil
import os

# 1 -- shutil.copyfileobj(src, dst)
# 必须以 open("xxxx","x") 的方式打开文件后写入，否则报错
# copyfileobj方法只会拷贝文件内容
# shutil.copyfileobj(open("old.txt", "r"), open("new.txt", "w"))
# os.system("cat old.txt new.txt")

# 2 -- shutil.copyfile(src, dct)
# 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
# shutil.copyfile("old.txt", "new1.txt")
# 如果有文件则会覆盖文件中的内容，没有则创建
# os.system("cat old.txt new.txt")

# 3 -- shutil.copymode(src, dst, *, follow_symlinks=True)
# 仅拷贝文件权限，文件的内容、组、用户均不变
# shutil.copymode("old.txt", "new1.txt")

# 4 -- shutil.copystat(src, dst, *, follow_symlinks=True)
# 拷贝文件状态的信息，文件必须存在，不copy改动时间
# shutil.copystat("old.txt", "new1.txt")
# os.system("stat old.txt new.txt")

# 5 -- shutil.copy(src, dst, *, follow_symlinks=True)
# 拷贝文件和状态信息，同样不copy改动时间
# shutil.copy("old.txt", "new2.txt")
# os.system("stat old.txt new2.txt")
# print("------------------------")

# 6 -- shutil.copy2(src,dct)
# 拷贝文件和状态信息
# shutil.copy("old.txt", "new2.txt")
# os.system("stat old.txt new2.txt")

# 7 -- shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件夹
# works2目录必须不存在，symlinks=True只copy链接文件，如果等于False就copy源文件，ignore等于不copy的文件或者目录
# os.system("tree works")
# shutil.copytree(
#     "works",
#     "works2",
#     symlinks=True,
# )
# os.system("tree works2")

# 8 -- shutil.rmtree(path, ignore_errors=False, onerror=None)
# 递归的去删除文件
# os.system("ls -d works2")
# shutil.rmtree("works2")
# os.system("ls -d works2")  # ls: works2: No such file or directory

# 9 -- shutil.move(src, dst, copy_function=copy2)
# 递归的去移动文件，它类似mv命令，其实就是重命名
# os.system("ls -ld works")
# drwxr-xr-x 3 SUe Administrators 0 Oct  8 17:59 works

# shutil.move("works", "works2")

# os.system("ls -ld works")
# ls: works: No such file or directory

# os.system("ls -ld works2")
# drwxr-xr-x 3 SUe Administrators 0 Oct  8 17:59 works2

# 10 -- shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径， 如：   tar_name  =>保存至当前路径 如：/Users/a6/tar_name =>保存至/Users/a6/
# format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir： 要压缩的文件夹路径（默认当前目录）
# owner： 用户，默认当前用户
# group： 组，默认当前组
# logger： 用于记录日志，通常是logging.Logger对象
