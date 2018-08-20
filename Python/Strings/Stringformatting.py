#Given an integer, n, print the following values for each integer i from 1 to n:
#1. Decimal
#2. Octal
#3. Hexadecimal (capitalized)
#4. Binary

#The four values must be printed on a single line in the order specified above for each i from 1 to n.
#Each value should be space-padded to match the width of the binary value of n.

#Input Format

#A single integer denoting n.

#1 <= n <= 99
#'''
#Sample Input
#10

#Sample Output

#    1     1     1     1
#    2     2     2    10
#    3     3     3    11
#    4     4     4   100
#    5     5     5   101
#    6     6     6   110
#    7     7     7   111
#    8    10     8  1000
#    9    11     9  1001
#   10    12     A  1010
#'''

n = int(input())
max_width = len('{0:b}'.format(n))
for number in range(1,n+1):
    for base in 'doXb':   #### watch the doXb size!!
        print('{0:{max_width}{base}}'.format(number, base=base, max_width=max_width).rstrip(), end=' ')
    print()
