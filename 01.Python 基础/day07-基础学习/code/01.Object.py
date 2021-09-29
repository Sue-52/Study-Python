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

# class Get_Salary:

#     def __call__(self, salary):
#         yearSalary = salary*12
#         daySalary = salary//22.5
#         hourSalary = daySalary//12

#         return dict(年薪=yearSalary,月薪=salary,日薪=daySalary,小时工=hourSalary)
# p1 = Get_Salary()
# print(p1(8000))

# class Person:
#     def hello_world(self):
#         print("Hello World")

# def say_Hi(name):
#     print("Hello,{0}".format(name))

# p1 = Person()
# # p1.say_Hi("Js")  # 'Person' object has no attribute 'say_Hi'

# Person.say = say_Hi
# # p1.say("!23")  # say_Hi() takes 1 positional argument but 2 were given
# Person.say("he")

# class Employee:

#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def  __work(self):
#         print("Good Good Work, Day Day Up")

# p1 = Employee("Allen",12)
# print(p1.name)  # Allen
# # print(p1.age)  # 'Employee' object has no attribute 'age'
# print(p1._Employee__age)  # 12
# # p1.__work()  # 'Employee' object has no attribute '__work'
# p1._Employee__work()  # Good Good Work, Day Day Up

# class Employee:

#     @property
#     def money(self):
#         print("working...")
#         return 20000

# p1 = Employee()  # 1. working...
# # p1.money()  # 'int' object is not callable
# # getMoney = p1.money
# # print(getMoney)  # 2. 20000
# print(p1.money)  # 3. working...  4. 20000

# class Employee:

#     def __init__(self,name,salary):
#         self.__name = name
#         self.__salary = salary

#     def get_salary(self):
#         # print("薪水：{0}".format(self.__salary))
#         return self.__salary

#     def set_salary(self,salary):
#         if 10000<salary<50000:
#             self.__salary = salary
#             print("薪资录入成功")
#         else:
#             print("薪资录入失败")

# p1 = Employee("Eason",30000)
# print("{0}薪资：{1}".format(p1._Employee__name, p1.get_salary()))  # Eason薪资：30000
# # p1.set_salary(3000) # 薪资录入失败
# p1.set_salary(20000)  # 薪资录入成功
# print("{0}薪资：{1}".format(p1._Employee__name, p1.get_salary()))  # Eason薪资：20000

# class Employee:

#     def __init__(self,name,salary):
#         self.__name = name
#         self.__salary = salary

#     @property
#     def salary(self):
#         # print("薪水：{0}".format(self.__salary))
#         return self.__salary

#     @salary.setter
#     def salary(self,salary):
#         if 10000<salary<50000:
#             self.__salary = salary
#             print("薪资录入成功")
#         else:
#             print("薪资录入失败")

# p1 = Employee("Eason",30000)
# print("{0}薪资：{1}".format(p1._Employee__name, p1._Employee__salary))  # Eason薪资：30000
# p1.salary = -2000  # 薪资录入失败
# p1.salary = 20000  # 薪资录入成功
# print("{0}薪资：{1}".format(p1._Employee__name, p1._Employee__salary))  # Eason薪资：20000

# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def say_hi(self):
#         print("Hello,Bro!!!")

# class Children(Person):

#     # 子类继承父类的属性
#     def __init__(self,name,age,score):
#         Person.__init__(self,name,age)
#         self.score = score

# print(
#     Children.mro()
# )  # [<class '__main__.Children'>, <class '__main__.Person'>, <class 'object'>]
# c1 = Children("Jason",23,100)
# c1.say_hi()  # Hello,Bro!!!  继承了父类的属性方法

# # 访问私有属性
# # 无法访问通过子类访问父类的私有属性
# print(c1._Person__age)  # 23
# print(dir(c1)) # ...各种实现

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def say_hi(self):
#         print("Hello,Bro!!!")

# class Children(Person):

#     # 子类继承父类的属性
#     def __init__(self, name, age, score):
#         Person.__init__(self, name, age)
#         self.score = score

#     def say_hi(self):
#         print("What's Up?")

# s1 = Children("Sue", 21, 100)
# s1.say_hi()  # What's Up?

# print(dir(Person))
# print(Children.mro())

# class A:
#     def aa(self):
#         print("----AA----")

#     def say(self):
#         print("Hello AAA")

# class B:
#     def bb(self):
#         print("----BB----")

#     def say(self):
#         print("Hello BBB")

# # 从左到右执行，A在前所以会先执行A类中的say.
# class C(A, B):
#     def cc(self):
#         print("----CC----")

# p1 = C()
# p1.cc()
# print(
#     C.mro()
# )  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# p1.say()

# class A:
#     def aa(self):
#         print(self)

# class B(A):
#     def bb(self):
#         # 方法一：直接获取
#         A.aa(self)  # <__main__.B object at 0x000001D4638F9F88>
#         # 方法二：super() 获取
#         super().aa()  # <__main__.B object at 0x000001D4638F9F88>
#         print(self)  # <__main__.B object at 0x000001D4638F9F88>

# b = B()
# b.bb()

# class Person:
#     def say(self):
#         print("你说话啊，你")

# class Chinese(Person):
#     def say(self):
#         print("中文....")

# class Japanese(Person):
#     def say(self):
#         print("日语....")

# class Amercian(Person):
#     def say(self):
#         print("英语....")

# def people(x):
#     if isinstance(x, Person):
#         x.say()
#     else:
#         print("请说人话")

# people(Chinese())
# people(Japanese())
# people(Amercian())
