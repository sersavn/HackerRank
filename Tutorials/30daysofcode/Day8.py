#Sample Input
#3
#sam 99912222
#tom 11122222
#harry 12299933
#sam
#edward
#harry

#Sample Output
#sam=99912222
#Not found
#harry=12299933

emptydict = dict()
for values in range(2*(int(input()))):
    z = input().split()
    if len(z) == 2:
        emptydict[z[0]] = z[1]
    if (len(z) == 1) and (z[0] in emptydict): # emptydict is faster than emptydict.keys()
        print(z[0], emptydict.get(z[0]), sep = '=')
    if (len(z) == 1) and (z[0] not in emptydict):
        print("Not found")


#e.g. in Python dict.keys() will create a new list that has all keys of your dict ...
#so if you have a dict with 1000 entries, you will have a new list with 1000 entries!
#so ... if x in dict is better than if x in dict.keys() :-)


#mydict = {'george':16,'amber':19}
#print(list(mydict.keys())[list(mydict.values()).index(16)])
#prints george

#print(mydict.keys())
#print(mydict.values())
#print(mydict.items())
