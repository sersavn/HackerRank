digits = list(map(int,input().split()))

def polycheck():
    for digit in digits:
        print(digit)
        digit = str(digit)
        digit2 = (digit[::-1])
        digit2 = int(digit2)
        digit = int(digit)
        if digit == digit2:
            return(True)
            break
        return(False)

print(polycheck())
