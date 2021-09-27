# class Student:
#     # 属性定义到构造方法中（固定写法）: __init__
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def say_score(self):
#         print(id(self))  # 2008779276616
#         print(self.name,"分数是：",self.score)

# s1 = Student("张三",93)
# print(id(s1))  # 2008779276616
# s1.say_score() # Student.say_score(s1)
# print(dir(s1))
# print(s1.__dict__)
# print(isinstance(s1.name,float))
# print(isinstance(s1.name,str))



# class Person:
#     pass

# print(type(Person))  # <class 'type'>
# print(id(Person))  # 1599475085048

# stu01 = Person()
# # s1 = stu01
# print(stu01)  # <__main__.Person object at 0x000002B454EC9E08>



# class Person:

#     # 类属性
#     school = "中加枫华国际学校"
#     tuition = 100000
#     count = 0

#     # 实例属性
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         Person.count = Person.count+1

#     # 实例方法
#     def get_score(self):
#         print("姓名：{0}；年龄：{1}；性别：{2}".format(self.name,self.age,self.gender))

# stu1 = Person("sue",22,"male")
# stu2 = Person("Jason",22,"male")
# stu3 = Person("Allen",22,"female")
# stu1.get_score()
# stu2.get_score()
# stu3.get_score()
# print("学校：{0}；学费：{1}".format(Person.school,Person.tuition))
# print("创建了{0}次实例".format(Person.count))




# class Person:

#     # 类属性
#     school = "中加枫华国际学校"
#     tuition = 100000
#     count = 0

#     # 实例属性
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.count = Person.count+1

#     # 静态实例
#     @staticmethod
#     def addNum(a,b):
#       print("{0}+{1}={2}".format(a,b,a+b))
#       return a+b

#     # 实例方法
#     def get_score(self):
#         print("姓名：{0}；年龄：{1}".format(self.name,self.age))

# stu1 = Person("sue", 22)
# stu1.get_score()
# Person.addNum(1,2)




# class Person:

#     def __del__(self):
#         print("销毁对象：{0}".format(self))

# p1 = Person()  # 5. 销毁对象：<__main__.Person object at 0x000001DFCD279FC8>
# print(id(p1))  # 1. 2060731260872
# p2 = Person()  # 3. 销毁对象：<__main__.Person object at 0x000001DFCD284088>
# print(id(p2))  # 2. 2060731302024
# del p2
# print("over")  # 4. over
# # print(id(p2))  # name 'p2' is not defined




class Get_Salary:

    def __call__(self, salary):
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//12

        return dict(年薪=yearSalary,月薪=salary,日薪=daySalary,小时工=hourSalary)
p1 = Get_Salary()
print(p1(8000))