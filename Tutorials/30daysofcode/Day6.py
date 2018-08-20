#Sample Input
#2
#Hacker
#Rank

#Sample Output
#Hce akr
#Rn ak

for i in range(int(input())):
    z = input()
    leng = len(z)
    le = list()
    lo = list()
    le.append(z[::2])
    lo.append(z[1::2])
    lo = '{}'.format(*lo)
    le = '{}'.format(*le)
    print(le + " " + lo)
