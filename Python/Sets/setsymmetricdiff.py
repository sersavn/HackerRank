#Sample Input
#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8

#Sample Output
#8


n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
s2 = set(map(int, input().split()))
print(len(s1.symmetric_difference(s2)))
