#import sys
def simpleArraySum(n, ar):
    # Complete this function
    ar = sum(ar)
    return(ar)
n = int(input("input n: ", ).strip())
print("n", n, type(n))
ar = list()
z = int()
while len(ar) < n:
    z = int(input("input z: ", ))
    ar.append(z)
    print("ar", ar, type(ar))
print(ar)
print("ar", ar, type(ar))
result = simpleArraySum(n, ar)
print("result", result, type(result))


#Somehow I need to get output ar and ar should consist of n elements
#In that case ar - numbers from keyboard, n - how many times I enter those numbers
#
