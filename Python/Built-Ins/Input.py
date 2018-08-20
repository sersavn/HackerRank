#Input Format
#The first line contains the space separated values of x and k.
#The second line contains the polynomial P.

#Output Format
#Print True if P(x)=k. Otherwise, print False.

#Sample Input
#1 4
#x**3 + x**2 + x + 1

#Sample Output
#True

x,k = map(int,input().split())
z = input()
if eval(z) == k: # or print(eval(z) == k), nuch shorter
    print('True')
else:
    print('False')
