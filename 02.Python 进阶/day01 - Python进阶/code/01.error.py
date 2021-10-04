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


class Sample():
    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type: ", exc_type)
        print("val: ", exc_val)
        print("tb: ", exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10


with Sample() as sample:
    sample.do_something()