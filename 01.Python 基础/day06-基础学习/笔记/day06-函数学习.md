## day 06 - 函数

函数是可重用的程序代码块。函数的作用，不仅仅可以实现代码的复用，更能实现代码的一致性。一致性指的是，只要修改函数的代码，则所有调用的该函数的地方都能体验。

编写函数只是对某种功能代码的封装，并增加了函数调用、传递参数、返回计算结果等内容

### 函数 - 简介 

1. 一个程序又一个个任务组曾；函数就是代表一个任务或者功能
2. 函数是代码服用的通用机制。

### 函数分类

1. 内置函数：使用的str()、list()、len()等都属于内置函数
2. 标准库函数：通过 import 语句导入的库
3. 第三方库函数：Python 社区提供的库，通过 import 导入并使用
4. 用户自定义函数：自己定义的函数，并只适用于自身需求所开发的函数

### 函数的定义和调用

语法格式：

~~~
def 函数名 ([参数列表]):
    '''文档字符串'''
    函数体、若干语句
~~~

要点：
1. 通过使用 def 来定义函数，然后就是一个空格和函数名
   1. Python 执行 def 时，会创建一个函数对象，并绑定到函数名变量上
2. 参数列表
   1. （）时形式参数列表。用多个参数则使用 ， 隔开
   2. 形式参数不需要声明类型，也不许哟啊指定函数返回值类型
   3. 无参数，也不许保留括号
   4. 实参列表必须与形参列表一一对应
3. return 返回值
   1. 如果函数体中包含 return 语句，则结束函数执行并返回值
   2. 如果函数体不包含 return 语句， 则返回 None 值
4. 调用函数之前，必须要先定义函数，既先调用 def 常见函数对象
   1. 内置函数对象会自动常见
   2. 标准库和第三方库函数，通过 import 导入模块时，会执行模块中的def语句

~~~python
def addNum():
  print("函数测试")
addNum()
~~~

#### 形参 & 实参

形参：代表的数据并不是真是的实际的参数、者、数据等，相当于一种变量
实参：输入的实际参数，将其赋给形参，形参在通过函数体中的语句进行一些列的操作

【操作】比较数字大小

~~~python
def compMax(a,b):
    if(a<b):
        print(b,"--b--打")
    else:
        print(a,"--a--打")

compMax(1, 21)  #2 1 --b--打
compMax(19, 8)  # 19 --a--打
~~~

#### 文档字符串（函数的注释）

通过使用 三个单引号或者三个双引号来实现。中间加入多行文字进行说明

【操作】测试

~~~python
def test():
  """测试注释"""
  print("Hello Function")
test()
~~~

可以使用 help() 函数输出函数中的文档字符串

~~~python
help(test)

# Help on function test in module __main__:
# test()

help(test.__doc__)

# No Python documentation found for '测试注释'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.
~~~

#### 函数返回值

return 返回值要点：

  1. 如果函数体中包含 return 语句，则结束函数执行并返回
  2. 如果函数体中不包含 return 语句，则返回 None
  3. 要返回多个返回值，使用列表、元组、字典、集合等存储起来

【操作】返回两数之和

~~~python
def fnAdd(a,b):
    return a+b

c = fnAdd(1,5)
print(c)  # 6
~~~

#### 函数也是对象

实际上，执行 def 所定义的函数后，系统就创建了相应的函数对象。

~~~python
def fnAdd(a,b):
    return a+b

print(fnAdd)  # <function fnAdd at 0x0000022B30DCD8B8>
print(id(fnAdd))  # 2115667351736
~~~

在执行 def 时，系统中会创建函数对象，并通过 fnAdd 这个变量进行引用


### 变量的作用域（全局变量和局部变量）

变量起作用的范围称之为变量的作用域，不同作用域内同名的变量之间互不影响。变量分为：全局变量、局部变量

**全局变量：**

1. 在函数和类定义之外声明的变量。作用域为定义的模块，从定义的位置直到模块
2. 全局变量降低了函数的通用性和可读性。应尽力避免全局变量的使用。
3. 全局变量一般做常数使用
4. 函数内要改变全局变量的值，使用 global 声名

**局部变量：**

1. 在函数体（包含形式参数）声明的变量
2. 局部变量的引用比全局变量快，优先
3. 如果局部变量和全局变量同同名，则在函数内隐藏全局变量，只是用同名的局部变量

【操作】作用域测试

~~~python
a = 100 # 全局变量
def f1():
    global a # 使用全局变量
    print(a)
    a = 300 # 修改了全局变量

f1()
print(a)
~~~

【操作】全局变量和局部变量同名

~~~python
a = 100
def f1():
    a = 200
    print(a) # 200

f1()
print(a) # 100
~~~

**使用 global() 输出全局变量**

【操作】全局变量和局部变量的效率差异

~~~python
import math
import time

def test01():
    start = time.time()
    for i in range(1000000):
        math.sqrt(30)
    end = time.time()
    print("耗时：{0}".format((end-start)))

def test02():
    b = math.sqrt
    start = time.time()
    for i in range(1000000):
        b(30)
    end = time.time()
    print("耗时：{0}".format((end-start)))


test01()  # 耗时：0.1767582893371582
test02()  # 耗时：0.14059734344482422
~~~

### 函数的传参

函数的参数传递本质上就是：从实参到形参的赋值操作。

所有的赋值操作都是 “引用的赋值” 。所以，Python 中参数的传递都是 “引用传递” ，不是 “值传递” 。

1. 对 “可变对象” 进行 “写操作”，直接作用于元年本对象的本身。
2. 对 “不可变对象” 进行 “写操作”，或产生一个新的 “对象空间” ，并用新的值填充这块空间（起到作用的语言的“值传递”效果，但不是“值传递”）

> 可变对象：字典、列表、集合、自定义的对象等
> 不可变对象：数字、字符串、元组、function

#### 传递可变对象的引用

传递参数时可变对象（Ex：列表、字自定义的其他可变对象），实际传递的还是对象的引用。在函数体中并不创建新的对象拷贝，二十可以直接修改所传递的对象。

【操作】参数传递：传递可变对象的引用

~~~python
a = [1,2,3,4,5]

def fn01(b): # b、m是同一个对象
    print(id(b)) # 2423060581192
    a.append(6) # 由于a为可变的对象，不创建对象拷贝可以直接进行修改
    print(id(b)) # 2423060581192

fn01(a)
print(id(a)) # 2423060581192
print(a) # [1, 2, 3, 4, 5, 6]
~~~

#### 传递不可变对象的引用

传递参数是不可变对象（Ex：int、float、字符串、元组、布尔值），实际传递的还是对象的引用。在“赋值操作”时，由于不可变对象无法修改，系统会新创建一个对象。

在调用时参数所处的地址永远是相同的，但是在进行赋值操作时就会改变其地址。

【操作】参数传递：不可变对象的引用

~~~python
a = 100
def fn01(b):
    print("b:", id(b))  # b: 140732072099168
    b += 100
    print("b:", id(b))  # b: 140732072102368
    print(b)  # 200

fn01(a)
print("a:", id(a))  # a: 140732072099168
~~~

显然，通过 id 值我们可以看到 b 和 a 已开始是同一个对象。给 b 赋值后，b 是新的对象。


#### 浅拷贝和深拷贝

内置函数为：copy() 浅拷贝、deepcopy() 深拷贝

浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用。
深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象。

【操作】浅拷贝

~~~python
import copy

a = [1,2,3,[4,5]]
b = copy.copy(a)
print("a:", id(a))  # a: 2261211812168
print("b:", id(b))  # b: 2261211769160
print("---------------")
b.append(6)
b[3].append(10)
print(a)  # [1, 2, 3, [4, 5, 10]]
print(b)  # [1, 2, 3, [4, 5, 10], 6]

~~~

![image-20210925173034254](./img/image-20210925173034254.png)


【操作】深拷贝

~~~python
def deepCopy():
    a = [1, 2, 3, [4, 5]]
    b = copy.deepcopy(a)
    print("a:", id(a))  # a: 2261211812168
    print("b:", id(b))  # b: 2261211769160
    print("---------------")
    b.append(6)
    b[3].append(10)
    print(a)  # [1, 2, 3, [4, 5]]
    print(b)  # [1, 2, 3, [4, 5, 10], 6]

deepCopy()
~~~

![image-20210925173543864](./img/image-20210925173543864.png)

#### 不可变对象含可变子对象

可以进行修改，并且地址不变

#### 参数的类型

**位置参数：**

函数调用时，实参默认按位置顺序传递，需要个数和形参匹配。按位置传递的参数，称为：“位置参数”

【操作】测试

~~~python
def fn01(a,b,c):
    return a+b+c

print(fn01(1,2,3)) # 6
print(fn01(1,3)) # 报错
~~~

**默认值参数：**

将形参设置为默认参数，这样传递参数时参数时可选的。默认值参数放在位置参数的后面

【操作】测试

~~~python
def fn01(a,b,c,d=10,e=11):
    return a+b+c+d+e

print(fn01(1,2,3))
print(fn01(1,3))
~~~

**命名参数：**

按照形参的名称传递参数

【操作】测试

~~~python
def fn01(a, b, c):
    print(a,b,c)
    return a + b + c

print(fn01(1, 2, 3)) # 位置参数
print(fn01(b=20,c= 12,a=13)) # 命名参数
~~~

**可变参数：**

指的是 “可变数量的参数”。分两种情况：

1. *param（一个星号），将多个参数收集到一个“元组”对象中。
2. **param（两个星号），将多个参数收集到一个“字典”对象中。

【操作】可变参数处理

~~~python
def fn01(a,b,*c):
    print(a,b,c)
fn01(8,9,19,20) # 8 9 (19, 20)


def fn02(a,b,**c):
    print(a,b,c)
fn02(8,9,name="sue",age=18) # 8 9 {'name': 'sue', 'age': 18}

def fn03(a,b,*c,**d):
    print(a,b,c,d)
fn03(8,9,20,12,"sue",name="sue",age=18,flag=True) # 8 9 (20, 12, 'sue') {'name': 'sue', 'age': 18, 'flag': True}
~~~

**强制命名参数：**

在带星号的“可变参数”后面增加新的参数，必须是“强制命名参数”

【操作】测试

~~~python
def fn01(*a,b,c):
    print(a,b,c)
# fn01(2,3,4) # 报错，由于 a 是可变参数，将2，3，4全部手机。造成了 b 和 c 没有赋值
fn01(2, 3, 4, b=13, c=10)  # (2, 3, 4) 13 10
~~~


#### Lambda 表达式

`lambda` 表达式可以用来声明匿名函数。lambda 函数是一种简单的、在同行中定义函数的方法。lambda 函数实际生成了一个函数对象

`lambda` 表达式只允许宝库哦一个表达式，不能包含复杂语句，该表达式的计算结果就是函数的返回值。

`lambda` 表达式语法：

~~~
lambda arg1,arg2,arg3 ...: <表达式>
~~~

> arg1、arg2、arg3 为函数的参数。
> <表达式> 箱单能与函数体。运算结果是：表达式的运算结果

【操作】lambda表达式使用

~~~python
fn = lambda a,b,c:a+b+c
print(fn)  # <function <lambda> at 0x000002465AC3E8B8>
print(fn(1, 2, 3))  # 6

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(
    g
)  # [<function <lambda> at 0x000001FB6F06EA68>, <function <lambda> at 0x000001FB6F06EAF8>, <function <lambda> at 0x000001FB6F06EB88>]
print(g[0](6), g[1](7), g[2](8))  # 12 21 32
~~~

#### eval() 函数

将字符串 str 当成有效的表达式来求值并返回计算机结果。

语法：

~~~
eval(source[,globals[,locals]]) -> value
~~~

**参数：**

source：一个 Python 表达式或者函数 compile() 返回的代码对象
globals：可选。必须是 dictionary
locals：可选。任意映射对象

【操作】eval() 函数使用

~~~python
eval("print('Hello')")  # Hello
a = 10
b = 20
c = eval("a+b")
print(c)  # 30

dict01 = dict(a=100,b=200)
d = eval("a+b",dict01)
print(d)  # 300
~~~

### 递归函数

递归函数指的是：自己调用自己的函数，在函数体内部直接或者间接的自己调用自己。递归类似于数学中的“数学归纳法”。每个递归函数必须包含两个部分：

1. 终止条件
   - 表示递归什么时候结束。一般用于返回值，不在调用自己。
2. 递归步骤
   - 把第 n 步的值和第 n-1 步相关联

递归函数由于会创建大量的函数对象，过量的消耗内存和运算能力。在处理大量数据时，谨慎使用。

【操作】递归计算阶乘

~~~python
def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)
for x in range(1,6):
    print(x,"!=",factorial(x))
~~~

结果：

~~~
1 != 1
2 != 2
3 != 6
4 != 24
5 != 120
~~~

### 嵌套函数

在函数内部定义函数

【操作】定义

~~~python
def fn01():
    print("running...01")

    def fn02():
        print("running...02")
    fn02()
fn01()
# running...01
# running...02
~~~

**使用情况：**

1. 封装 - 数据隐藏
   - 外部无法访问 “嵌套数据”
2. 贯彻 DRY（Don't Repeat Yourself）原则
   - 嵌套函数，可以让我们在函数内部避免重复代码。
3. 闭包


~~~python
def get_name(isChinese,name,familyName):
    def print_name(a,b):
        print("{0} {1}".format(a,b))
    
    if isChinese:
        print_name(familyName,name)
    else:
        print_name(name,familyName)

get_name(True,"傲","苏")
get_name(False,"Edmond","Dantes")
~~~

#### nonlocal 关键字

nonlocal 用来声明外层的局部变量。
global 用来声明全局变量。

【操作】测试

~~~python
def outer():
    a = 100
    def inner():
        nonlocal a
        print("inner a: {0}".format(a))
        a = 200
    inner()
    print("outer a: {0}".format(a))
outer()
~~~

**作用：将外部函数的变量适用于内部变量中，并且内部变量进行修改时，外部的变量也会发生变化**

### LEGB 规则

Python 在查找 “名称” 时，是按照 LEDG 规则查找的： 
Local --> Enclosed --> Global --> Built in

`Local`     指的是函数或者类的方法内部
`Enclosed`  指的是嵌套函数（闭包）
`Global`    指的是波块中的全局变量
`Built in`  指的是 Python 为自己保留的特殊名称

如果某个 name 映射在局部（local）命名空间中没有找到，接下拉就会在闭包作用域（enclosed）进行搜索，以此类推。

最后都没找到就会生成一个 NameError

​    