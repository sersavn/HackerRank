
s = input()

for letters in s:
    x = 0
    if letters.isalpha() is True :
        x += 1
        print(letters)
if x != 0 : print("True")
else : print("False")
