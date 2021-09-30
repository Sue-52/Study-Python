# 类的引入使用： from 文件名 import 类名
from restaurant import Restaurant

p1 = Restaurant("米其林", "精品菜")
p1.describe_restaurant()

# 案例二：
from restaurant import User
from restaurant import Privilege

p2 = User("Sue")
p2.get_name()
p3 = Privilege("student")
p3.get_privilege()