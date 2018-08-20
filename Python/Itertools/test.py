import itertools
answer = int()
listone = list()
element2 = list()
def square(list):
    return [i ** 2 for i in list]
K, M = map(int,input().split())
for randomvalue in range(K):
    element = list(sorted(map(int,input().split())))
    element = (square(element))
    print(element)
