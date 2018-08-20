#In Python, a string of text can be aligned left, right and center.

#This method returns a left aligned string of length width.

#.ljust(width)

#This method returns a left aligned string of length width.

width = 20
print('HackerRank'.ljust(width,'-'))

#.center(width)

#This method returns a centered string of length width.

width = 20
print('HackerRank'.center(width,'-'))

#.rjust(width)

#This method returns a right aligned string of length width.

width = 20
print('HackerRank'.rjust(width,'-'))

#Task

#You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
#Your task is to replace the blank (______) with rjust, ljust or center.

#Input Format

#A single line containing the thickness value for the logo.
