# try:
#     print(5 / 0)
# except:
#     print("You can't divide by zero!")

# try:
#     print(" step 1 ")  # 1. step 1
#     a = 3 / 0
#     print(" step 2 ")
# except BaseException as e:
#     print(" step 3 ")  #  2. step 3
#     print(e)  # 3. division by zero

# print(" step 4 ")  #  4. step 4

# -------------------------------------------------------
# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a) / float(b)
# except BaseException as e:
#     print(e)
# else:
#     print("结果：", c)
# finally:
#     print("我一直执行中...")

# print("结束")

# -------------------------------------------------------
# class Sample:
#     def __enter__(self):
#         print("in__enter__")
#         return "Foo"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("out_exit")

# def get_Sample():
#     return Sample()

# with get_Sample() as sample:
#     print("Sample：", sample)

# -------------------------------------------------------
# class Sample():
#     def __enter__(self):
#         print('in enter')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("type: ", exc_type)
#         print("val: ", exc_val)
#         print("tb: ", exc_tb)

#     def do_something(self):
#         bar = 1 / 0
#         return bar + 10

# with Sample() as sample:
#     sample.do_something()

# -------------------------------------------------------
# import traceback
# try:
#     print("first step")
#     num = 3 / 0
# except:
#     traceback.print_exc()

# -------------------------------------------------------
# 将异常信息输出到指定文件
# import traceback
# try:
#     print("first step")
#     num = 3 / 0
# except:
#     with open(
#             "d:/00.study/Study-Python/02.Python 进阶/day01 - Python进阶/code/errorMsg.txt",
#             "a") as f:
#         traceback.print_exc(file=f)


# -------------------------------------------------------
# 自定义异常类
class LongNameException(Exception):
    def __init__(self, len):
        self.len = len

    def __str__(self):
        if (self.len < 2):
            print("姓名长度为：{0}。长度过短".format(self.len))
        elif (self.len > 5):
            print("姓名长度为：{0}。长度过长".format(self.len))


def get_name():
    name = input("请输入姓名：")
    print(type(len(name)))
    if len(name) < 2:
        raise LongNameException(len(name))
    elif len(name) > 5:
        raise LongNameException(len(name))
    else:
        print(name)


get_name()