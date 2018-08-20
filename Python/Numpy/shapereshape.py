import numpy

arr = list(map(int, input().split()))
arr = numpy.array(arr)
arr.shape = (3,3)
print(arr)
