#Sample Input
#1222311

#Sample Output
#(1, 1) (3, 2) (1, 3) (2, 1)

s = str(input())
import itertools
emptylist = list()
for value, number in itertools.groupby(s):
    numberlist = list(number)
    listlength = len(numberlist)
    #print("value, listlength", listlength, value)
    pair = tuple((listlength, (int(value))))
    #print("typepar", type(pair))
    emptylist.append(pair)
print(*emptylist)
