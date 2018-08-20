#Input Format

#The first line contains space separated integers N,M  and P.
#The next N lines contains the space separated elements of the P columns.
#After that, the next M lines contains the space separated elements of the P columns.

#Sample Input
#4 3 2
#1 2
#1 2
#1 2
#1 2
#3 4
#3 4
#3 4

#Sample Output
#[[1 2]
# [1 2]
# [1 2]
# [1 2]
# [3 4]
# [3 4]
# [3 4]]



import numpy
a1 = list()
a2 = list()
N,M,P = list(map(int, input().split()))
for elements in range(N):
    a1.append(list(map(int, input().split())))
for elements2 in range(M):
    a2.append(list(map(int, input().split())))
a1 = numpy.array(a1)
a2 = numpy.array(a2)
print(numpy.concatenate((a1, a2), axis = 0))

#print(a1)


#print(numpy.concatenate((array_1, array_2), axis = 0))
