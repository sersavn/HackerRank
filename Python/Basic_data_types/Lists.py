#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.


#The first line contains an integer, n, denoting the number of commands.
#Each line i of the b subsequent lines contains one of the commands described above.

#Constraints

#The elements added to the list must be integers.
#Output Format

#For each command of type print, print the list on a new line.

#Sample Input

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print

#Sample Output

#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]


lst = list()
y = 0
N = int(input()) # how many iterations
while N > y :
    y = y + 1
    z = input()
    z = z.split()
    if z[0] == 'insert' :
        lst.insert(int(z[1]), int(z[2]))
    elif z[0] == 'print' :
        print(lst)
    elif z[0] == 'remove' :
        lst.remove(int(z[1]))
    elif z[0] == 'append' :
        lst.append(int(z[1]))
    elif z[0] == 'sort' :
        lst.sort()
    elif z[0] == 'pop' :
        lst.pop()
    elif z[0] == 'reverse' :
        lst.reverse()
    #continue

#arr = [1,2,3]
#arr.remove(3)
