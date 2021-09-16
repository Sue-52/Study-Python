dic = {
  "name":"sue",
  "age":21,
  "gender":"male"
}
print(dic)

dic1 = dict(name="hhh",age=22)
print(dic1)

a = ["name","age","gender"]
b = ["zyc",21,"student"]
dic3 = dict(zip(a,b))
print(dic3)  # {'name': 'zyc', 'age': 21, 'gender': 'student'}

dic4 = dic.fromkeys(["name","age","job"])
print(dic4)  # {'name': None, 'age': None, 'job': None}

getDic1 = dict(name="sue",age=26,job="programmer")
print(getDic1["name"])  # sue
# print(getDic1["gender"]) # 报错

print(getDic1.get("name"))  # sue
print(getDic1.get("gender", "male"))  # male

print(getDic1.items()) # dict_items([('name', 'sue'), ('age', 26), ('job', 'programmer')])

print(getDic1.keys())  # dict_keys(['name', 'age', 'job'])

print(getDic1.values())  # dict_values(['sue', 26, 'programmer'])

print(len(getDic1))  # 3

print("name" in getDic1)  # True
print("gender" in getDic1)  # False

addDic1 = {
  "name":"jyc",
  "age":21,
  "gender":"famale",
  "job":"student"
}
addDic1["age"]=22;
addDic1["address"] = "上海市xxx"
print(
    addDic1
)  # {'name': 'jyc', 'age': 22, 'gender': 'famale', 'job': 'student', 'address': '上海市xxx'}

a = {
  "name":"sue",
  "Age":33
}
b = {
  "Age":22
}
a.update(b)
print(a) # {'name': 'sue', 'Age': 22}

delDic1 = {
  "name":"Jason",
  "age":22,
  "gender":"male",
  "hobby":"basketball"
}

del(delDic1["age"])
print(delDic1)  # {'name': 'Jason', 'gender': 'male', 'hobby': 'basketball'}

# delDic1.clear()
# print(delDic1)  # {}

delDic2 = delDic1.pop("gender")
print(delDic2)  # male

delDic3 = {
  "name":"Jason",
  "age":22,
  "gender":"male",
  "hobby":"basketball"
}
delDic3.popitem()
print(delDic3)  # {'name': 'Jason', 'age': 22, 'gender': 'male'}

pak = {
  "name":"sue",
  "age":22,
  "hobby":"frisbee"
}
a,b,c = pak
print(a, b, c)  # name age hobby
a,b,c = pak.items()
print(a, b, c)  # ('name', 'sue') ('age', 22) ('hobby', 'frisbee')
a,b,c = pak.values()
print(a, b, c)  # sue 22 frisbee

a = {}
a["name"] = "Aqua"
print(bin(hash("name")))  # -0b1011100010010000111001100111011000001110110110111010110111110
