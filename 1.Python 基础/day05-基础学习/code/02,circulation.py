# num = 0
# while num<10:
#     num+=1
#     print(num, end="\t")


num = 0
sum_all = 0
sum_even = 0
sum_odd = 0
while num <=100:
    sum_all+=num
    if(num % 2 ==0):
        sum_even+=num
    else:
        sum_odd+=num
    num+=1

print("总数是：{0}，偶数和是：{1}，奇数和是：{2}".format(sum_all, sum_even, sum_odd))
