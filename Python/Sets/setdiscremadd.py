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
s = set(map(int, input().split()))
for operations in range(int(input())):
    command = input().split()
    if command[0] == "pop" :
        s.pop()
    if command[0] == "remove" :
        s.remove(int(command[1]))
    if command[0] == "discard" :
        s.discard(int(command[1]))
print(sum(s))
