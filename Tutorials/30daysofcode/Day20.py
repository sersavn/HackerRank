y = 0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
print('initial list', a)
while a != sorted(a):
    for x in range (len(a)-1):
        if a[x] > a[x+1]:
            y += 1
            a[x], a[x+1] = a[x+1], a[x]
print('Array is sorted in', y, 'swaps.')
print('First Element:', min(a))
print('Last Element:', max(a))

#print(min(a))
#print(max(a))
