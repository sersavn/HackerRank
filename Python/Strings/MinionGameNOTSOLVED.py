#Sample Input:
#BANANA

#Sample Output
#Stuart 12

word = str(input())
length = len(word)
print(len(word))
Kevin = list()
Stuart = list()
M = 0
while M <= length:
    N = 1
    print("M,N", M, N)
    while N <= length and M < length:
        if N <= M :
            N = M + 1
        print("inner", word[M:N])
        if word[M] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") :
            Kevin.append(word[M:N])
        else :
            Stuart.append(word[M:N])
        N = N + 1
    M = M + 1
print("Kevin", Kevin)
print("Stuart", Stuart)
if len(Kevin) == len(Stuart):
    print("Draw")
elif len(Stuart) > len(Kevin):
    print("Stuart", len(Stuart))
elif len(Stuart) < len(Kevin):
    print("Kevin", len(Kevin))
