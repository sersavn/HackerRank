#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

#You are given an immutable string, and you want to make changes to it.

#One solution is to convert the string to a list and then change the value.

#>>> string = "abracadabra"
#>>> l = list(string)
#>>> l[5] = 'k'
#>>> string = ''.join(l)
#>>> print string
#abrackdabra

#Another approach is to slice the string and join it back.

#>>> string = string[:5] + "k" + string[6:]
#>>> print string
#abrackdabra

#Sample Input

#abracadabra
#5 k

#Sample Output

#abrackdabra


def mutate_string(string, position, character):
    return(string[:position] + character + string[position+1:]) #+1 bcs value is replaced, not add

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
