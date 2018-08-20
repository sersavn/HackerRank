#Objective
#In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

#Task
#Given an integer, n , print its first 10 multiples. Each multiple n x i (where 1<= i <= 10) should be printed
#on a new line in the form: n x i = result.

#Input Format

#A single integer, n.

#Constraints
#2<= i <= 20

#Output Format

#Print 10 lines of output; each line  (where 1 <= i <= 10) contains the result of n x i in the form:
#n x i = result.

n = int(input().strip())
for i in range(1,11) :
    i = int(i)
    n = int(n)
    x = n * i
    x = str(x)
    i = str(i)
    n = str(n)
    print(str(n + " x " + i + " = " + x))
