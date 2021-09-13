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