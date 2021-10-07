# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
# 该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
for x in range(100, 1000):
    single_digit = x % 10  # 获取整除于10的个位数
    tens_digit = x // 10 % 10  # 获取十位数
    hundreds_digit = x // 100  # 获取百位数
    if x == single_digit**3 + tens_digit**3 + hundreds_digit**3:
        print(x)
