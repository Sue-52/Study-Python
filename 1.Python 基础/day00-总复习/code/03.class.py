class Restaurant:

    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0}-{1}".format(self.name,self.cuisine_type))

    def open_restaurant(self):
        print("餐馆正在营业")

first = Restaurant("刘家祥","湘菜")
first.describe_restaurant()
first.open_restaurant()
print("-------------------------------------------------")


