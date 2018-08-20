#You are given n numbers. Store them in a list and find the second largest number.

#The first line contains n. The second line contains an array A[] of n integers each separated by a space.

#sample imput
#5
#2 3 6 6 5

#sample output
#5

n = int(input())
arr = map(int, input().split())
arr = list(arr)
print(arr, type(arr))
if len(arr) > n :
        arr = arr[:-1]
x = (max(arr))
while x == max(arr) :
    arr.remove(x)
    print(arr)
print(max(arr))
