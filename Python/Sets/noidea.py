meter = 0
lenarr, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
intersec = setA.intersection(setB)
for values in intersec:
    setA.remove(values)
    setB.remove(values)
for i in arr :
    if i in setA:
        meter += 1
    if i in setB:
        meter -= 1
print(meter)
