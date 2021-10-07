'''
素数指的是只能被1和自身整除的正整数（不包括1）。
'''
import math

for num in range(2, 11):  # 第一层循环获取要判断的数字
    is_prime = True
    # 二层循环获取要判断的数值到2之间是否能有整除的数
    for factor in range(2, int(math.sqrt(num)) + 1):
        # 能够整出则不是素数
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')