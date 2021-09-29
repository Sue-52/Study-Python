set1 = {1,2,3,4,5}
print(set1)  # {1, 2, 3, 4, 5}

set1.add(20)
print(set1)  # {1, 2, 3, 4, 5, 20}

set2 = ["a","b","c",12,34]
set3 = set(set2)
print(set3)  # {'b', 34, 'c', 12, 'a'}

set3.remove("a")
print(set3)  # {34, 'c', 12, 'b'}
set3.clear()
print(set3)  # set()

a = {1,2,3,"six"}
b = {4,5,"six",7}
print(a | b)  # 并集 {1, 2, 3, 4, 5, 7, 'six'}
print(a & b)  # 交集 {'six'}
print(a - b)  # 差集 {1, 2, 3}
print(a.union(b))  # 并集 {1, 2, 3, 4, 5, 7, 'six'}
print(a.intersection(b))  # 交集 {'six'}
print(a.difference(b))  # 差集 {1, 2, 3}
