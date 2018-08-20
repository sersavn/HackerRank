#Sample Input

#hello world

#Sample Output

#Hello World


def capitalize(string):
    string = string.split(' ')
    new_text = []
    for letters in string:
        cap = letters.capitalize()
        new_text.append(cap)
    return (" ".join(new_text))
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)


#account spaces and add them to ts!
