#Input Format
#The first line of input contains the space separated values of  and .
#The next  lines contains  space separated integers.

#Output Format
#Compute the min along axis  and then print the max of that result.

#Sample Input
#4 2
#2 5
#3 7
#1 3
#4 0

#Sample Output
#3

import numpy
N,M = map(int,input().split())
arr = numpy.array([input().split() for _ in range(N)],int)
arrmin = numpy.min(arr,axis = 1)
arrmax = numpy.max(arrmin)
print(arrmax)
