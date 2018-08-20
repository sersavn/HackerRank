list1 = [7, 2, 3, 10, 12]
list2 = [-1, 1, -5, 4, 6]
print("len", len(list2))
map(lambda x, y: x*y, list1, list2)
print(list(map(lambda x, y: x*y, list1, list2)))
