#Sample Input
#1 2
#3 4

#Sample Output
#(1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

l1 = sorted(list(map(int, input().split())))
l2 = sorted(list(map(int, input().split())))
result = (list(product(l1, l2)))
print(" ".join(map(str, result)))
