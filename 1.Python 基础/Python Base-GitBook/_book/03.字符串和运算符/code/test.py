import time

time01 = time.time()
a = ""
for i in range(1000000):
    a+="sxt"

time02 = time.time()
print("运算时间："+str(time02-time01)) # 运算时间：0.4503052234649658

# 使用 
time03 = time.time()
li = []
for i in range(1000000):
    li.append("xxx")

time04 = time.time()
print("运算时间："+str(time04-time03)) # 运算时间：0.18450689315795898

