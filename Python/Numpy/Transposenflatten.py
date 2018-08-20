import numpy

arr = []
n,m = list(map(int, input().split()))
for elements in range(n):
    emptylist = list(map(int, input().split()))
    arr.append(emptylist)
arr = numpy.array(arr)
arr.shape = (n, m)
print(arr.transpose())
print(arr.flatten())
