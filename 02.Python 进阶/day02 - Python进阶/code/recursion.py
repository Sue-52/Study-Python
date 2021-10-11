# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)

# print(factorial(10))

# 递归输出目录树
import os

allFiles = []


def get_all_files(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            get_all_files(filepath, level + 1)
        allFiles.append("\t" * level + filepath)


get_all_files("works2", 0)
for f in reversed(allFiles):
    print(f)