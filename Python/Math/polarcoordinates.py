#Sample Input
#1+2j

#Sample Output

#2.23606797749979 
#1.1071487177940904



import cmath

x = complex(input())
print(abs(x))
print(cmath.phase(x))
print(cmath.polar(x))
