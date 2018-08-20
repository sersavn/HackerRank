#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8

#Sample Output

#13


n = int(input())
l1 = list(map(int, input().split()))
s1 = set(l1)
l2 = (list(s1))*n
print(int((sum(l2) - sum(l1))/(n-1)))
