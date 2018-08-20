#Factorial

#Sample Input
#3

#Sample Output
#6

#!/bin/python3

import math

def factorial(n):
    return(math.factorial(n))

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
