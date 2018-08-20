
#Sample Input
#3 1000
#2 5 4
#3 7 8 9
#5 5 7 8 9 10
#
#Sample Output
#206




import itertools
answer = int()
listone = list()
element2 = list()
def square(list):
    return [i ** 2 for i in list]
K, M = map(int,input().split())
for randomvalue in range(K):
    element = list(sorted(map(int,input().split()))[:1])
    element = (square(element))
    print("elem", element)
    listone.append(element)
print(listone)
suspectedarea = list(itertools.product(*listone))
for sublists in suspectedarea:
    print(sum(sublists))
    if ((sum(sublists))%M) > answer:
        answer = ((sum(sublists))%M)
print(answer)


#"The next lines each contains an integer Ni followed by Ni space separated integers denoting the elements in the list."
#So the first number is the number of numbers. We don't need that.
