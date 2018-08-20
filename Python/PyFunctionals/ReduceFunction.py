#Sample Input 0
#3
#1 2
#3 4
#10 6

#Sample Output 0
#5 8

#Explanation 0

#Required product is 1/2*3/4*10/6 = 5/8


##wrong

from functools import reduce
from fractions import Fraction


emptylist = []

for lines in range(int(input())):
    values = list(map(int,input().split()))
    values = values[0]/values[1]
    emptylist.append(values)

#l = (reduce(lambda x, y : x * y, emptylist))
#l = Fraction(-8, 80)
#print(l.numerator, l.denominator)
print(emptylist)

"""
from fractions import Fraction
from functools import reduce
def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
"""
