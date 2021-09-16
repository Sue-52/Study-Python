# num = input("请输入数字：")
# if int(num) <= 10:
#     print("数字太小了")
# else:
#     print(num)

# print("数字小于10" if int(num) <= 10 else "数字大于10")

score = int(input("请输入分数："))
grade = ""
if score < 60:
    grade="不及格"
elif score <70:
    grade="及格"
elif score < 80:
    grade="良"
elif score < 90:
    grade="优秀"
else:
    grade="完美"

print("分数是{0}，等级是{1}".format(score,grade))