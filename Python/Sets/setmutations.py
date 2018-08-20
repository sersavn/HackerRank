n = int(input())
s = set(map(int, input().split()))
for operations in range((int(input()))):
    command = input().split()
    if command[0] == "intersection_update" :
        sn = set(map(int, input().split()))
        s.intersection_update(sn)
    if command[0] == "update" :
        sn = set(map(int, input().split()))
        s.update(sn)
    if command[0] == "symmetric_difference_update" :
        sn = set(map(int, input().split()))
        s.symmetric_difference_update(sn)
    if command[0] == "difference_update" :
        sn = set(map(int, input().split()))
        s.difference_update(sn)
print(sum(s))
