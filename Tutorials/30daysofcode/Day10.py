#Sample Input 1
#5

#Sample Output 1
#1

#Sample Input 2
#13

#Sample Output 2
#2

#Explanation

#Sample Case 1:
#The binary representation of  is , so the maximum number of consecutive 's is .

#Sample Case 2:
#The binary representation of  is , so the maximum number of consecutive 's is .


simpleint = int(input())
binint = "{0:b}".format(simpleint)
binint = str(binint)
binint = binint.split("0")
print(len(max(binint)))
