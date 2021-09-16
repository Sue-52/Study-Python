tuple1 = (1,2,3,4,5)
tuple2 = 1,2,3,4,5,6
print(tuple1,tuple2)

tuple3 = 123,
print(tuple3)  # (123,)

tuple4 = tuple()
tuple5 = tuple("!23")
tuple6 = tuple(range(4))
tuple7 = tuple([2,3,4,5])
print(tuple4)  # ()
print(tuple5)  # ('!', '2', '3')
print(tuple6)  # (0, 1, 2, 3)
print(tuple7)  # (2, 3, 4, 5)

visit1 = tuple("abcdefg")
print(visit1[0]) #

visit2 = tuple([10,30,40,21,12,87,90])
sorted(visit2)
print(visit2)  # (10, 30, 40, 21, 12, 87, 90)

first = [1,2,3]
second = [4,5,6]
third = [7,8,9]
last = zip(first,second,third)
print(last) # <zip object at 0x000001C1FB4CDD88>
print(list(last))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

s = (x*2 for x in range(5))

print(s.__next__())  # 0
print(s.__next__())  # 2
print(s.__next__())  # 4

