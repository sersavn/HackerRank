#Sample Input 0
#3

#Sample Output 0
#3

#Sample Input 1
#za

#Sample Output 1
#Bad String


S = input().strip()
try :
    int(S)
    print(S)
except:
    print('Bad String')
