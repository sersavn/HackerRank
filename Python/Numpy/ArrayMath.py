#Sample Input
#1 4
#1 2 3 4
#5 6 7 8
#
#Sample Output
#[[ 6  8 10 12]]
#[[-4 -4 -4 -4]]
#[[ 5 12 21 32]]
#[[0 0 0 0]]
#[[1 2 3 4]]
#[[    1    64  2187 65536]]

import numpy

Alist = []
Blist = []

N,M = map(int,input().split())

for ements in range(N):
    A = list(map(int,input().split()))
    Alist.append(A)

for ements in range(N):
    B = list(map(int,input().split()))
    Blist.append(B)

A = numpy.array(Alist,int)
B = numpy.array(Blist,int)

print(A+B)
print(A-B)
print(A*B)
print((A/B).astype(int))
print(A%B)
print(A**B)
