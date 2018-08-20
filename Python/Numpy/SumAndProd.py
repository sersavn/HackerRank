#Sample Input
#2 2
#1 2
#3 4

#Sample Output
#24

#Explanation
#The sum along axis 0 = [4 6]
#The product of this sum = 24

import numpy
N,M = map(int,input().split())
#z = numpy.array((input().split()) for _ in range(N))
z = numpy.array([input().split() for _ in range(N)],int)
print(z)

npsum = numpy.sum(z, axis = 0)
#print(npsum)
npprod = numpy.prod(npsum)
print(npprod)
