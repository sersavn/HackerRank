#Sample Input

#7
#UK
#China
#USA
#France
#New Zealand
#UK
#France

#Sample Output

#5

s = set()
for countries in range(int(input())):
    country = str(input())
    print(country, type(country))
    s.add(country)
print(len(s))
