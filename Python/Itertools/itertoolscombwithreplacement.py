#Sample Input
#hACK 2

#Sample Output
#AA
#AC
#AH
#AK
#CC
#CH
#CK
#HH
#HK
#KK

S, k = input().split()
from itertools import combinations_with_replacement
answer = list(combinations_with_replacement(sorted(S),int(k)))
for elements in answer:
    print(*elements, sep = '')
