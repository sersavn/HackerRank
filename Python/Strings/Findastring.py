#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

#NOTE: String letters are case-sensitive.

#Input Format

#The first line of input contains the original string. The next line contains the substring.

#Sample Input

#ABCDCDC
#CDC

#Sample Output

#2

def count_substring(string, sub_string):
    x = 0 # used to move forward part of the string that is being cut
    c = 0 # used to count amount of sub_string in string that is cut
    print(len(sub_string))
    print(string.find(sub_string))
    while x < len(string) :
        if sub_string == string[x:(len(sub_string)+x)] :
            c += 1
            x += 1
            print("sub_string, string", sub_string, string[x:(len(sub_string)+x)])
        else :
            x += 1
            print("sub_string, string", sub_string, string[x:(len(sub_string)+x)])
    return(c)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
