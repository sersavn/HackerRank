#Task
#Perform append, pop, popleft and appendleft methods on an empty deque d.

#Input Format
#The first line contains an integer N, the number of operations.
#The next N lines contains the space separated names of methods and their values.

#Output Format
#Print the space separated elements of deque d.

#Sample Input
#6
#append 1
#append 2
#append 3
#appendleft 4
#pop
#popleft

#Sample Output
#1 2

from collections import deque
d = deque()
for doesentmatter in range(int(input())):
    commands = input().split()
    if commands[0] == 'pop':
        d.pop()
    if commands[0] == 'popleft':
        d.popleft()
    if commands[0] == 'append':
        d.append(commands[1])
    if commands[0] == 'appendleft':
        d.appendleft(commands[1])
print(*d)
