class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0}-{1}".format(self.name, self.cuisine_type))

    def open_restaurant(self):
        print("餐馆正在营业")


class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("姓名：{0}".format(self.__name))


class Privilege:
    def __init__(self, privilege):
        self.__privilege = privilege

    def get_privilege(self):
        print("地位：{0}".format(self.__privilege))