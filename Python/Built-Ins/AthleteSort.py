n, m = map(int,input().split())
tuplahouse=list()
for lines in range(n):
    tupla = tuple(map(int, input().split()))
    tuplahouse.append(tupla)
k = int(input())
sortt = sorted(tuplahouse, key = lambda header: header[k]) #K - number of the table header
for elements in sortt:
    print(*elements)
