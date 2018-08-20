#Sample Input
#
#10
#2 3 4 5 6 8 7 6 5 18
#6
#6 55
#6 45
#6 55
#4 40
#18 60
#10 50

#Sample Output
#200

#Explanation
#Customer 1: Purchased size 6 shoe for $55.
#Customer 2: Purchased size 6 shoe for $45.
#Customer 3: Size 6 no longer available, so no purchase.
#Customer 4: Purchased size 4 shoe for $40.
#Customer 5: Purchased size 18 shoe for $60.
#Customer 6: Size 10 not available, so no purchase.

from collections import Counter
income = 0
shoesnum = int(input())
shoeslist = Counter(map(int, input().split()))
for customers in range(int(input())):
    shoesize, shoesprice = map(int, input().split())
    if shoeslist[shoesize] > 0 :
        shoeslist[shoesize] += -1
        income += shoesprice
print(income)
