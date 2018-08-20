s = set(map(int, input().split()))
for sets in range((int(input()))):
    s1 = set(map(int, input().split()))
    if ((s.union(s1)) == s) and (s != s1) :
        continue
    else :
        print("False")
        quit()
print("True")
