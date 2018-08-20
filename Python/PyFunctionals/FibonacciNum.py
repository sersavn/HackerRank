n = int(input())
fibolist = [0,1]
if n == 0: print(fibolist[0])
if n == 1: print(fibolist[0:2])
if n > 1:
    for elements in range(2,n+1):
        print('elements', elements)
        el1 = fibolist[elements-2]
        el2 = fibolist[elements-1]
        el = el1+el2
        fibolist.append(el)
print(fibolist)
