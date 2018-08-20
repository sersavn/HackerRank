import itertools
meter = 0
N = int(input())
string = str(input()).split()
string = "".join(string)
K = int(input())
Kletters = string[0:K]
letlist = list()
combolist = list(itertools.combinations(string,K))
print(combolist, type(combolist))
aset = set("a")
print(aset)
for elements in combolist:
    elements = set(elements)
    check = aset.intersection(elements)
    if bool(check) == True:
        meter += 1
print(meter/len(combolist))
