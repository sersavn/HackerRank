#Input Format
#The first line contains an integer N.
#N is the total number of integers in the list.
#The second line contains the space separated list of N integers.

#Output Format
#Print True if all the conditions of the problem statement are satisfied.
#Otherwise, print False.

#Sample Input
#5
#12 9 61 5 14

#Sample Output
#True
#
#Explanation
#Condition 1: All the integers in the list are positive.
#Condition 2: 5 is a palindromic integer.

digitsnum = int(input())
digits = list(map(int,input().split()))

def polycheck():
    for digit in digits:
        if digit < 0:
            return(False)
            break
        digit = str(digit)
        digit2 = (digit[::-1])
        digit2 = int(digit2)
        digit = int(digit)
        if digit == digit2:
            return(True)
            break
    return(False)

def elementscheck():
    if all(digit > 0 for digit in digits):
        return(True)
    else:
        return(False)

print(polycheck() and elementscheck()) == True
