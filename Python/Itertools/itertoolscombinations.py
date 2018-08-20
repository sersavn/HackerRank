#Sample Input
#
#hACK 2
#Sample Output

#A
#C
#H
#K
#AC
#AH
#AK
#CH
#CK

S, k = input().split()
import itertools
#print(answer)
for krange in range(1,int(k)+1):
    answer = list(itertools.combinations(sorted(S), krange))
    for elements in answer:
        print(*elements, sep = '')
