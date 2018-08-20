#Python has built-in string validation methods for basic data.
#It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

#You are given a string .
#Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

#Sample Input

#qA2

#Sample Output

#True
#True
#True
#True
#True

s = input()

#print 'ab123'.isalnum() #This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#print 'abcD'.isalpha() #This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#print '1234'.isdigit() #This method checks if all the characters of a string are digits (0-9).
#print 'abcd123#'.islower() #This method checks if all the characters of a string are lowercase characters (a-z).
#print 'ABCD123#'.isupper() #This method checks if all the characters of a string are uppercase characters (A-Z).

print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))
