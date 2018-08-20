#Input Format
#The first line contains the space separated value of the coefficients in P.
#The second line contains the value of x.
#
#Output Format
#Print the desired value.
#
#Sample Input
#1.1 2 3
#0
#
#Sample Output
#3.0

import numpy
#print(numpy.poly([1.1,2,3]))
#print(numpy.roots([1,2,1]))
arr = list(map(float, input().split()))
xpoint = int(input())
print(numpy.polyval(arr, xpoint))
