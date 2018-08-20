#Sample Input

#HAck 2
#Sample Output

#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH

S, k = input().split()
import itertools
answer = sorted(list(itertools.permutations(S, int(k))))
for objects in answer:
    print(*objects, sep = '')

#print(("\n".join(map(str,answer))))
