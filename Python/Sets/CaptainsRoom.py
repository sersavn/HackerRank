#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8

#Sample Output

#13


n = int(input())
l1 = list(map(int, input().split()))
s1 = sorted(set(l1))
for rooms in s1:
    if l1.count(rooms) == 1 :
        print(rooms)
        break
