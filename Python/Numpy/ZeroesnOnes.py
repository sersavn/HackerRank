#Sample Input 0
#3 3 3

#Sample Output 0
#[[[0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]]
#[[[1 1 1]
#  [1 1 1]
#  [1 1 1]]
#
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
#
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]]

import numpy
numbers = list(map(int, input().split()))
print(numpy.zeros((numbers), dtype = numpy.int))
print(numpy.ones((numbers), dtype = numpy.int))
