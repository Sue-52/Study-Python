print(ord("A"))
print(ord("苏"))
print(chr(66))

str1 = 'sease'
str1 = "sdgfsad"

str3 = ''' name="sue" age="21" gender="male" '''
print(str3)

str4="  "
print(len(str4))

str5="asdfsdf"
print(len(str5))

str6= '123''456';
print(str6)

str7 = "123"*3
print(str7)

print("Hello",end=" ");
print("World")

# name=input("请输入姓名：")
# print(name)

num = 123123
print(str(num))

str8 = "abcdefg"
print(str8[1]) # b

str9 = "1,2,3,4,5,6,7"
str10 = str9.replace("1","8")
print(str9)
print(str10)


str11 = "abcdefghijklmn"
print(str11[0:1:1]) # a
print(str11[1:]) # bcdefghijklmn
print(str11[:1]) # a

str12 = "to be or not to be"
print(str12[::-1]) # eb ot ton ro eb ot

str13 = "life is terrible"
print(str13.split()) # ['life', 'is', 'terrible']
print(str13.split("is")) # ['life ', ' terrible']

str14 = ["123","456","789"];
print("+".join(str14)) # 123+456+789
# print(str14.join()) # 123+456+789

str15 = "姓名：{name},年龄：{age}"
str16 = str15.format(name="Sue",age=18)
print(str16) # 姓名：Sue,年龄：18