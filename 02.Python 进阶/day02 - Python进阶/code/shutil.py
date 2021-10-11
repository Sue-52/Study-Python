# shutil 模块的使用
# import shutil
# import os

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