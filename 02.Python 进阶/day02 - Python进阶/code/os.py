# -------------------------------------------------
# os 打开记事本

# from genericpath import getatime
import os

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
os.makedirs("works/some/www")
path = os.getcwd()
# print(path)
file_lists = os.walk(path)
# print(list(file_lists))
for dirpaths, dirnames, filenames in file_lists:
    # print(dirpaths)
    # print(dirnames)
    # print(filenames)
    for dirP in dirnames:
        # print(dirP)
        print(os.path.join(dirpaths, dirP))

    for names in filenames:
        print(os.path.join(dirpaths, names))
