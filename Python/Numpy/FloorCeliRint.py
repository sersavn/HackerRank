#Input Format
#A single line of input containing the space separated elements of array A.
#
#Output Format
#On the first line, print the floor of A.
#On the second line, print the ceil of A.
#On the third line, print the rint of A.

import numpy
A = list(map(float,input().split()))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
