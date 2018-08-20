#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#10
#pop
#remove 9
#discard 9
#discard 8
#remove 7
#pop
#discard 6
#remove 5
#pop
#discard 5

#Sample Output

#4

#Output Format

#Print the sum of the elements of set  on a single line.


n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
s2 = set(map(int, input().split()))
print(len(s1.difference(s2)))
