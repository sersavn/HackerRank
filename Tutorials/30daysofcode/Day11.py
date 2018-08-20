#Sample Input
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0


#Sample Output
#19

#The hourglass with the maximum sum (19) is:
#2 4 4
#  2
#1 2 4

twoDarray = list()
z = None
for rows in range(6):
    twoDarray.append(list(map(int, input().split())))
print(twoDarray)
listarr = list(number for oneDarray in twoDarray for number in oneDarray)
print(listarr)
for x in range(4):
    for y in range(4):
        shortcalc = sum(listarr[(0+x+6*y):(3+x+6*y)]+listarr[(7+x+6*y):(8+x+6*y)]+listarr[(12+x+6*y):(15+x+6*y)])
        print(shortcalc)
        if z == None:
            z = shortcalc
        if shortcalc > z :
            z = shortcalc
print(z)
