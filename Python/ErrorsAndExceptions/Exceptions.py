#Task
#You are given two values a and b.
#Perform integer division and print a/b.

#Input Format
#The first line contains T, the number of test cases.
#The next T lines each contain the space separated values of a and b.

#Output Format
#Print the value of a/b.
#In the case of ZeroDivisionError or
#ValueError, print the error code.


for n in range(int(input())):
    try:
        a,b = map(int,input().split())
    except ValueError as v:
        print("Error Code:" ,v)
        continue
    try:
        print(int(a/b))
    except ZeroDivisionError as z:
        print("Error Code: integer division or modulo by zero")
