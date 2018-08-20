#Task

#Given an integer,n ,and n space-separated integers as input, create a tuple, t, of those  integers.
#Then compute and print the result of hash(t).

#Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

#Input Format

#The first line contains an integer, n, denoting the number of elements in the tuple.
#The second line contains n space-separated integers describing the elements in tuple t.

#Output Format

#Print the result of hash(t).

#Sample Input

#2
#1 2

#Sample Output (shulpk bibi hash function)

#3713081631934410656

#

y = 0
lst = list()
N = int(input()) # how many iterations check Find2ndLrgstNum or Nested lists
while N > y :
    y = y + 1
    z = input().split(' ')
    lst.append(z)
mytup = tuple(lst)
print(mytup, type(mytup))
