#Given the names and grades for each student in a Physics class of N students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format

#The first line contains an integer, N, the number of students.
#The 2N subsequent lines describe each student over 2 lines;
#the first line contains a student's name, and the second line contains their grade.

#Sample Input

#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#Sample output

#Berry
#Harry


lst = [[str(input("Enter name ", )), float(input("Enter mark ",))] for numbers in range(int(input('input range ',)))]
Notworst = sorted(list(set(marks for names, marks in lst)))[1] # set is needed to exclude situation when [1] will not work (>1 worst grades)
students = sorted(list(name for name ,mark in lst if mark == Notworst)) # to make that fuckers by alphabet
for ppl in students:
    print(ppl)
