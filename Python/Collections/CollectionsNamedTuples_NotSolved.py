#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

#collections.namedtuple()

#Basically, namedtuples are easy to create, lightweight object types.
#They turn tuples into convenient containers for simple tasks.
#With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

#Example
#Code 01
#from collections import namedtuple
#Point = namedtuple('Point','x,y')
#pt1 = Point(1,2)
#pt2 = Point(3,4)
#dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
#print dot_product
#11

#Code 02
#from collections import namedtuple
#Car = namedtuple('Car','Price Mileage Colour Class')
#xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
#print xyz
#Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
#print xyz.Class
#Y

#Sample Input
#TESTCASE 01
#5
#ID         MARKS      NAME       CLASS
#1          97         Raymond    7
#2          50         Steven     4
#3          91         Adrian     9
#4          72         Stewart    5
#5          80         Peter      6

#Sample Output
#TESTCASE 01
#78.00

from collections import namedtuple
rowsnum = int(input())
#headers = namedtuple('headers', map(str, input().split(' ')))
#print(headers)
headers2 = str(input().split(' '))
print(headers2)
namedt = namedtuple('Row', headers2)
print(namedt)
#for rows in range(rowsnum):
#    Z = headers(input())
    #Z = headers(map(str, input().split(' ')))
#    print(Z)

#for
#for n in range(1+int(input())):
    #input()
#Row = namedtuple('Row', ['ID', 'MARKS', 'NAME', 'CLASS'])
#R = Row(ID = 1, MARKS = (97,50), NAME = 'Raymond', CLASS = 7)
#print(R)

#data = namedtuple(input(), input())
#print(data)
