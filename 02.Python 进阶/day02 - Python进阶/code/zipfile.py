# zipFile 模块的使用
import zipfile

# 1. is_zipfile 检查文件是否是一个 zip 文件
# print(zipfile.is_zipfile("works2.zip"))  # True
# print(zipfile.is_zipfile("works2"))  # False

# 2. ZipFile(filename[,mode[,compression[,allowZip64]]])
# print(zipfile.ZipFile("works2.zip", "r"))
# <zipfile.ZipFile filename='works2.zip' mode='r'>

# 3. close() 关闭文件，结束时必须要有
# z = zipfile.ZipFile("works2.zip", "r")
# z.close()
# print(z)  # <zipfile.ZipFile [closed]>

# 4. extract(member,path=None,pwd=None) 从 zip 中提取一个文件
# print(z.extract("works2/s.txt", path=None, pwd=None))

# 5. extractall(path[,pwd]) 将文件按照 namelist 中的目录结构从当前 zip 中提取出来并放到指定目录下
# z.extractall("works2")
# z.close()

# 6. namelist() 返回一个列表，内容是 zip 文件中所有子文件的path
# print(z.namelist())  # ['works2/', 'works2/some/', 'works2/some/www/']
# z.close()

# 7. infolist() 返回一个列表，内容是每个 zip 文件中子文件的 ZipInfo 对象
# print(z.infolist())
# [<ZipInfo filename='works2/' external_attr=0x10>, <ZipInfo filename='works2/some/' external_attr=0x10>, <ZipInfo filename='works2/some/www/' external_attr=0x10>]
# z.close()

# 8. printdir() 将 zip 文件的目录结构打印到 stdout 上，包括了 path，修改时间和大小
# print(z.printdir())
# File Name                                             Modified             Size
# works2/                                        2021-10-08 17:59:50            0
# works2/some/                                   2021-10-08 17:59:50            0
# works2/some/www/                               2021-10-08 17:59:50            0
# z.close()

# 9. open(name[,mode[,pwd]]),获取一个子文件的文件对象，可以将其用来read、readline、write等操作

# 10. setpassword(psw)，设置zip文件的密码
# z.setpassword(123456)

# 11. testzip() 读取 zip 中所有文件
# a = z.testzip()
# print(a is None)

# 12. write(filename[,arcname[,compression_type]]) 将其与文件写入 zip 中
# z = zipfile.ZipFile("works2.zip", "w")
# z.write("files.py")
# z.write("os.py")
# z.write("shutil.py")
# z.close()
