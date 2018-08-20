#Input Format
#The first line contains the space separated elements of array A.
#The second line contains the space separated elements of array B.

#Output Format
#First, print the inner product.
#Second, print the outer product.
#
#Sample Input
#0 1
#2 3
#
#Sample Output
#3
#[[0 0]
# [2 3]]

import numpy
A = numpy.array([input().split()],int)
B = numpy.array([input().split()],int)
print(numpy.inner(A,B)[0][0])
print(numpy.outer(A,B))
