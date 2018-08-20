#Sample Input
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0

#Sample Output
#19


import numpy
z = None
arr = list()
for rows in range(6):
    arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
for xcomponent in range(4):
    for ycomponent in range(4):
        #print(sum(sum(a[(xcomponent+0):(xcomponent+3),(ycomponent+0):(ycomponent+3)])))
        if z == None :
            z = sum(sum(arr[(xcomponent+0):(xcomponent+3),(ycomponent+0):(ycomponent+3)]))
        if z < sum(sum(arr[(xcomponent+0):(xcomponent+3),(ycomponent+0):(ycomponent+3)])):
            z = sum(sum(arr[(xcomponent+0):(xcomponent+3),(ycomponent+0):(ycomponent+3)]))
print(z)
