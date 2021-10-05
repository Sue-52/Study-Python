## Python进阶 -- 异常

在实际工作中，当我们遇到的情况不可能是非常完美的。如：写某个模块，用户输入不一定符合你的要求；程序要打开某个文件，但是这个文件可能不存在或者文件格式不对等等问题。

软件程序在运行的过程中，非常可能遇到这些问题。我们称之为：异常，英文：Exception。

如果要拷贝一份文件，在没有异常机制下的情况下，我们要考虑各种的异常情况。

【操作】伪代码使用 if 处理程序中可能出现的情况

~~~python
if "d:/a.txt" 这个文件存在：
    if e盘的空间大于 a.txt 文件长度：
        if 文件复制一半 IO 流断了：
            停止copy，输出：IO流出问题
        else：
            copyFile("d:/a.txt","e:/a.txt")
    else:
        print("e盘空间不够存放a.txt")
else:
    print("a.txt不存在")
~~~

坏处：

1. 逻辑代码和错误代码放在了一起
2. 程序员本身需要考虑的例外情况较复杂，对程序员本身要求高

`Python` 本身提供了给予我们处理异常机制的方法，如下（示意）：

~~~python
try:
    copyFile("d:/a.txt","e:/a.txt")
except:
    print("文件无法拷贝")
~~~

### 异常机制本质

异常指程序运行过程中出现的非正常现象，列如用户输入错误、除数为零、需要处理的文件不存在、数组下标越界等。

所谓异常处理，就是指程序在出问题时依然可以正常执行剩余的程序，而不会因为异常而终止程序执行。

Python中，引进了很多用来描述和处理异常的类，成为异常类。异常类定义中包含了该类异常的信息和对异常类进行处理的方法。

~~~
BaseException                                 --Base classes
 +-- Exception                                --Base classes
 |    +-- ArithmeticError                     --Base classes
 |    |    +-- FloatingPointError             --Concrete exceptions
 |    |    +-- OverflowError                  --Concrete exceptions
 |    |    +-- ZeroDivisionError              --Concrete exceptions
 |    +-- AssertionError                      --Concrete exceptions
 |    +-- AttributeError                      --Concrete exceptions
 |    +-- BufferError                         --Base classes
 |    +-- EOFError                            --Concrete exceptions
 |    +-- ImportError                         --Concrete exceptions
 |    |    +-- ModuleNotFoundError            --Concrete exceptions
 |    +-- LookupError                         --Base classes
 |    |    +-- IndexError                     --Concrete exceptions
 |    |    +-- KeyError                       --Concrete exceptions
 |    +-- MemoryError                         --Concrete exceptions
 |    +-- NameError                           --Concrete exceptions
 |    |    +-- UnboundLocalError              --Concrete exceptions
 |    +-- OSError                             --Concrete exceptions
 |    |    +-- BlockingIOError                --OS
 |    |    +-- ChildProcessError              --OS
 |    |    +-- ConnectionError                --OS
 |    |    |    +-- BrokenPipeError           --OS
 |    |    |    +-- ConnectionAbortedError    --OS
 |    |    |    +-- ConnectionRefusedError    --OS
 |    |    |    +-- ConnectionResetError      --OS
 |    |    +-- FileExistsError                --OS
 |    |    +-- FileNotFoundError              --OS
 |    |    +-- InterruptedError               --OS
 |    |    +-- IsADirectoryError              --OS
 |    |    +-- NotADirectoryError             --OS
 |    |    +-- PermissionError                --OS
 |    |    +-- ProcessLookupError             --OS
 |    |    +-- TimeoutError                   --OS
 |    +-- ReferenceError                      --Concrete exceptions
 |    +-- RuntimeError                        --Concrete exceptions
 |    |    +-- NotImplementedError            --Concrete exceptions
 |    |    +-- RecursionError                 --Concrete exceptions
 |    +-- StopIteration                       --Concrete exceptions
 |    +-- StopAsyncIteration                  --Concrete exceptions
 |    +-- SyntaxError                         --Concrete exceptions
 |    |    +-- IndentationError               --Concrete exceptions
 |    |         +-- TabError                  --Concrete exceptions
 |    +-- SystemError                         --Concrete exceptions
 |    +-- TypeError                           --Concrete exceptions
 |    +-- ValueError                          --Concrete exceptions
 |    |    +-- UnicodeError                   --Concrete exceptions
 |    |         +-- UnicodeDecodeError        --Concrete exceptions
 |    |         +-- UnicodeEncodeError        --Concrete exceptions
 |    |         +-- UnicodeTranslateError     --Concrete exceptions
 |    +-- Warning                             --Warnings
 |         +-- DeprecationWarning             --Warnings
 |         +-- PendingDeprecationWarning      --Warnings
 |         +-- RuntimeWarning                 --Warnings
 |         +-- SyntaxWarning                  --Warnings
 |         +-- UserWarning                    --Warnings
 |         +-- FutureWarning                  --Warnings
 |         +-- ImportWarning                  --Warnings
 |         +-- UnicodeWarning                 --Warnings
 |         +-- BytesWarning                   --Warnings
 |         +-- ResourceWarning                --Warnings
 +-- GeneratorExit                            --Concrete exceptions
 +-- KeyboardInterrupt                        --Concrete exceptions
 +-- SystemExit                               --Concrete exceptions
~~~

![Python异常类继承图](http://c.biancheng.net/uploads/allimg/190819/2-1ZQ9154321244.gif)

测试：

~~~python
print(5 / 0)
~~~

控制台输出：

~~~
Traceback (most recent call last):
  File "d:\00.study\Study-Python\02.Python 进阶\day01 - Python进阶\code\01.error.py", line 6, in <module>
    print(5 / 0)
ZeroDivisionError: division by zero
~~~

**Python 中一切皆对象，异常也采用对象的方法来处理。过程：**

1. **抛出异常**：在执行一个方法时，如果发生异常，则这个方法生成代表该异常的一个对象，停止当前执行路径，并把异常对象提交给解释器。
2. **捕获异常**：解释器得到该异常后，寻找相应的代码进行异常处理

~~~python
try:
    print(5 / 0)
except:
    print("You can't divide by zero!")
~~~


### `try ... except ...` 结构

`try...except` 是最长肌氨的异常处理结构。结构如下：

~~~
try:
    被监视的可能引发异常的语句块
except:
    异常处理与语句块
~~~

try块包含着可能引发异常的代码，except块则用来捕获和处理发生的异常。执行的时候，如果 try 中没有引发异常，则跳过 except 模块执行后续代码，如果 try模块中发生异常，则跳过后续代码，进入 except模块中处理异常，处理完毕后执行后续代码。

【操作】遇到异常的执行顺序：

~~~python
try:
    print(" step 1 ")  # 1. step 1
    a = 3 / 0
    print(" step 2 ")
except BaseException as e:
    print(" step 3 ")  #  2. step 3
    print(e)  # 3. division by zero

print(" step 4 ")  #  4. step 4
~~~

###  `try .多个. except ...` 结构

该结构可以进行多个捕获异常，建议也是使用多次捕获异常（按照先子类后父类的顺序），并且针对性的写出异常处理代码。为了避免遗漏可能出现的异常，可以在最后增加 BaseException。结构如下：

~~~
try:
    被监视的可能引发异常的语句块
except BaseException as xxx:  # Exception 1
    处理 Exception1 的语句块
except BaseException as xxx:  # Exception 2
    处理 Exception2 的语句块
...
~~~

【操作】测试

~~~python
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
    print(c)
except ValueError:
    print("异常，不能将字符串转化为数字")
except ZeroDivisionError:
    print("异常，不能除以0")
except NameError:
    print("异常，变量不存在")
except BaseException as e:
    print(e)
~~~

### `try ... except ... else` 结构

`try...except..else` 结构增加加了“else模块”。如果 try 中没有抛出异常，则执行 else 模块。如果 try 中抛出异常，则执行 except 模块，不执行else

【操作】测试

~~~python
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print("结果：", c)
~~~

### `try ... except ... finally` 结构

`try ... except ... finally` 结构中，finally模块无论是否发生异常都会被执行；通常用来释放try模块中申请的资源。

【操作】测试

~~~python
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print("结果：", c)
finally:
    print("我一直执行中...")

print("结束")
~~~

结果
~~~
请输入被除数：4
请输入除数：2
结果： 2.0
我一直执行中...
结束
~~~


### 常见异常解决

| 异常名称                  | 描述                                               |
| :------------------------ | :------------------------------------------------- |
| BaseException             | 所有异常的基类                                     |
| SystemExit                | 解释器请求退出                                     |
| KeyboardInterrupt         | 用户中断执行(通常是输入^C)                         |
| Exception                 | 常规错误的基类                                     |
| StopIteration             | 迭代器没有更多的值                                 |
| GeneratorExit             | 生成器(generator)发生异常来通知退出                |
| StandardError             | 所有的内建标准异常的基类                           |
| ArithmeticError           | 所有数值计算错误的基类                             |
| FloatingPointError        | 浮点计算错误                                       |
| OverflowError             | 数值运算超出最大限制                               |
| ZeroDivisionError         | 除(或取模)零 (所有数据类型)                        |
| AssertionError            | 断言语句失败                                       |
| AttributeError            | 对象没有这个属性                                   |
| EOFError                  | 没有内建输入,到达EOF 标记                          |
| EnvironmentError          | 操作系统错误的基类                                 |
| IOError                   | 输入/输出操作失败                                  |
| OSError                   | 操作系统错误                                       |
| WindowsError              | 系统调用失败                                       |
| ImportError               | 导入模块/对象失败                                  |
| LookupError               | 无效数据查询的基类                                 |
| IndexError                | 序列中没有此索引(index)                            |
| KeyError                  | 映射中没有这个键                                   |
| MemoryError               | 内存溢出错误(对于Python 解释器不是致命的)          |
| NameError                 | 未声明/初始化对象 (没有属性)                       |
| UnboundLocalError         | 访问未初始化的本地变量                             |
| ReferenceError            | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
| RuntimeError              | 一般的运行时错误                                   |
| NotImplementedError       | 尚未实现的方法                                     |
| SyntaxError               | Python 语法错误                                    |
| IndentationError          | 缩进错误                                           |
| TabError                  | Tab 和空格混用                                     |
| SystemError               | 一般的解释器系统错误                               |
| TypeError                 | 对类型无效的操作                                   |
| ValueError                | 传入无效的参数                                     |
| UnicodeError              | Unicode 相关的错误                                 |
| UnicodeDecodeError        | Unicode 解码时的错误                               |
| UnicodeEncodeError        | Unicode 编码时错误                                 |
| UnicodeTranslateError     | Unicode 转换时错误                                 |
| Warning                   | 警告的基类                                         |
| DeprecationWarning        | 关于被弃用的特征的警告                             |
| FutureWarning             | 关于构造将来语义会有改变的警告                     |
| OverflowWarning           | 旧的关于自动提升为长整型(long)的警告               |
| PendingDeprecationWarning | 关于特性将会被废弃的警告                           |
| RuntimeWarning            | 可疑的运行时行为(runtime behavior)的警告           |
| SyntaxWarning             | 可疑的语法的警告                                   |
| UserWarning               | 用户代码生成的警告                                 |

### with 上下文管理器

finally 模块由于是否发生异常都会执行，通常我们释放资源的代码。其实，我们可以同各国 with 上下文管理，更方便的实现释放资源的操作。

结构如下

~~~
with context_expr [as var]:
    语句块
~~~

with 上下文管理可以自动管理资源，在 with 代码块执行完毕后自动还原进入该改代码之前的现场或上下文。不论何种原因跳出 with 模块，不论是否有异常，总能保证资源正常释放。极大简化了工作，在文件操作、网络通信的场合非常常用。

with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。

【操作】with上下文管理操作

~~~python
with open("d:/bb.txt") as f:
    content = f.readline()
    print(content)
~~~

~~~python
file = open("１.txt")
data = file.read()
file.close()
~~~

上面代码存在２个问题：
（１）文件读取发生异常，但没有进行任何处理；
（２）可能忘记关闭文件句柄；

**改进：**

~~~python
try:
    f = open('xxx')
except:
    print('fail to open')
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()
~~~

虽然这段代码运行良好，但比较冗长。
而使用with的话，能够减少冗长，还能自动处理上下文环境产生的异常。如下面代码：

~~~python
with open("１.txt") as file:
    data = file.read()
~~~

#### with 工作原理

1. 紧跟 with 后面的语句被求值后，返回对下你给的 “-enter-()” 方法被调用，这个方法的返回值将被赋值给 as 后面的变量；
2. 当 with 后面的代码块全部被执行完后，将调用前面返回对象 “-exit-()” 方法

示例：

~~~python
class Sample:
    def __enter__(self):
        print("in_enter_")
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("out_exit")


def get_Sample():
    return Sample()


with get_Sample() as sample:
    print("Sample：", sample)
~~~

可以看到，整个运行过程如下：
（１）enter()方法被执行；
（２）enter()方法的返回值，在这个例子中是”Foo”，赋值给变量sample；
（３）执行代码块，打印sample变量的值为”Foo”；
（４）exit()方法被调用；

【注：】exit()方法中有３个参数， exc_type, exc_val, exc_tb，这些参数在异常处理中相当有用。
exc_type：　错误的类型
exc_val：　错误类型对应的值
exc_tb：　代码中错误发生的位置

示例代码：

~~~python
class Sample():
    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type: ", exc_type)
        print("val: ", exc_val)
        print("tb: ", exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10

with Sample() as sample:
    sample.do_something()
~~~

结果：

~~~
in enter
type:  <class 'ZeroDivisionError'>
val:  division by zero
tb:  <traceback object at 0x000001563EEC7F08>
~~~

### trackback 模块使用

【示例】使用 Traceback 输出异常信息

~~~python
import traceback
try:
    print("first step")
    num = 3 / 0
except:
    traceback.print_exc()
~~~

结果：

~~~
first step
Traceback (most recent call last):
  File "d:\00.study\Study-Python\02.Python 进阶\day01 - Python进阶\code\01.error.py", line 67, in <module>
    num = 3 / 0
ZeroDivisionError: division by zero
~~~

**用于想控制台那样输出整体的报错信息，但是执行进程并不会中断**

【操作】使用 taceback 将异常信息写入到指定文件

~~~python
import traceback
try:
    print("first step")
    num = 3 / 0
except:
    with open(
            "d:/00.study/Study-Python/02.Python 进阶/day01 - Python进阶/code/errorMsg.txt",
            "a") as f:
        traceback.print_exc(file=f)
~~~

> 在进行写入的时候会自行创建出指定文件并写入

### 自定义异常类

程序开发中，需要我们自定义异常类。自定义异常类一般都是运行时异常，通常继承 Exception 或其子类即可。命名一般以 Error、Exception为后缀。

自定义异常由 raise 语句主动抛出。

【操作】测试

~~~python
# 自定义异常类
class LongNameException(Exception):
    def __init__(self, len):
        self.len = len

    def __str__(self):
        if (self.len < 2):
            print("姓名长度为：{0}。长度过短".format(self.len))
        elif (self.len > 5):
            print("姓名长度为：{0}。长度过长".format(self.len))

def get_name():
    name = input("请输入姓名：")
    print(type(len(name)))
    if len(name) < 2:
        raise LongNameException(len(name))
    elif len(name) > 5:
        raise LongNameException(len(name))
    else:
        print(name)

get_name()
~~~