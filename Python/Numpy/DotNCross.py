#Input Format
#The first line contains the integer N.
#The next N lines contains N space separated integers of array A.
#The following N lines contains N space separated integers of array B.

#Output Format
#Print the matrix multiplication of A and B.

import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.dot(A, B))
#print(numpy.cross(A, B))
