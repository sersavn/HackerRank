n = int(input())
l1 = list(map(int, input().split()))
s1 = set(l1)
l2 = (list(s1))*n
print(int((sum(l2) - sum(l1))/(n-1)))
