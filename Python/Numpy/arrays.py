#Sample Input
#1 2 3 4 -8 -10

#Sample Output
#[-10.  -8.   4.   3.   2.   1.]

import numpy
b = list(map(float, input().split(" ")))
a = (numpy.array(b))[::-1]
print(a)
