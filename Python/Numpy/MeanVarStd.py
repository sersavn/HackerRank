#Task
#
#You are given a 2-D array of size NxM.
#Your task is to find:

#The mean along axis 1
#The var along axis 0
#The std along axis None

#Sample Input
#2 2
#1 2
#3 4
#
#Sample Output
#[ 1.5  3.5]
#[ 1.  1.]
#1.11803398875

import numpy
N,M = map(int,input().split())
arr = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr, axis = None))
