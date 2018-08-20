#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2

#def swap_case(self, text):

#    return

#Sample Input

#HackerRank.com presents "Pythonist 2".

#Sample Output

#hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    new_text = []
    for letters in s:
        if letters.islower() is True :
            new_text.append(letters.upper())# *new_text - * - unpack operator
        if letters.islower() is False :
            new_text.append(letters.lower())
    return(''.join(new_text)) # in order to convert list format
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
