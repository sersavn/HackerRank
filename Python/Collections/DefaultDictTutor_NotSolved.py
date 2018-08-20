#Sample Input
#5 2
#a
#a
#b
#a
#b
#a
#b

#Sample Output
#1 2 4
#3 5
#Explanation

#'a' appeared 3 times in positions 1, 2  and 4.
#'b' appeared 2 times in positions 3 and 5.
#In the sample problem, if 'c' also appeared in word group , you would print -1.

from collections import defaultdict
defdict, groupB = defaultdict(list), list()

n,m = map(int, input().split())
for elements in range(n):
    defdict[input()].append(elements+1)
for elements in range(m):
    groupB.append(str(input()))

for symbol in groupB:
    if symbol in defdict:
        print(*defdict[symbol])
    else:
        print("-1")
