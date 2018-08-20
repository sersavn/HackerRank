#Input Format
#One line of input: an integer .

#Constraints

#Output Format
#A list on a single line containing the cubes of the first  fibonacci numbers.
#
#Sample Input
#5
#
#Sample Output
#[0, 1, 1, 8, 27]

n = int(input())
cube = lambda x: x**3
fibolist = [0,1]

def fibonacci(n):
    if n == 0:
        return list([])
    if n == 1:
        return list([n-1])
    if n > 1:
        for elements in range(2,n):
            print('elements', elements)
            el1 = fibolist[elements-2]
            el2 = fibolist[elements-1]
            el = el1+el2
            fibolist.append(el)
    return fibolist
print(list(map(cube, fibonacci(n))))
