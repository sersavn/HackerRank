#Sample Input
#4
#1 4 3 2

#Sample Output

#2 3 4 1


n = int(input())
arr = map(int, input().split())
arr = list(arr)
while len(arr) > n :
        arr = arr[:-1]
arr = (arr[::-1])
print(*arr)
#print(*arr)
#while x < max(arr) :
#    arr.remove(x)

#    print(sorted(arr), reverse = True)
#print(max(arr))
#4
# 1 4 3 2
