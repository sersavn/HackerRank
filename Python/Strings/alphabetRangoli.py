

#Sample Input

#5

#Sample Output

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

n = int(input())
arr = list()
cen = int(1+4*(n-1))
for p in range(n) :        #10 will be replaced by n
    arr.append(chr(97+p))
#print(arr[9:10])
#print(arr[8:10])
#print(arr[7:10])
#print('RIGHT UP')
#for p in reversed(range(10)):
#    print(arr[p:10])
#print('LEFT UP')
#for p in reversed(range(10)):
#    print(list(reversed(arr[(p+1):(10)])))
#print('UP')
for p in reversed(range(n)):
    x = (list(reversed(arr[(p+1):(n)])) + (arr[p:n]))
    #print(list(reversed(arr[(p+1):(10)])) + (arr[p:10]))
    print(('-'.join(x)).center(cen,"-"))
#print('RIGHT DOWN')
#for p in (range(10)):
#    print(arr[p:10])
#print('LEFT DOWN')
#for p in (range(10)):
#    print(list(reversed(arr[(p+1):(10)])))
#print('DOWN')
for p in (range(1,n,1)):
    x = (list(reversed(arr[(p+1):(n)])) + (arr[p:(n)]))
    print(('-'.join(x)).center(cen,"-"))
