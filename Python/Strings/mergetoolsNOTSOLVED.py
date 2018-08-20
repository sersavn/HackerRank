word = str(input())
result = []
length = len(word)
dividedby = int(input())
substringlength = int(length/dividedby)
x = 0
while x < dividedby:
    substring = word[substringlength*x:substringlength*(x+1)]
    print(substring)
    for uniqueletter in substring:
        if uniqueletter not in result:
            result.append(uniqueletter)
    print("".join(result))
    result[:] = []
    x = x + 1
