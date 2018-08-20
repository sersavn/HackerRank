#Sample Input
#5 3
#89 90 78 93 80
#90 91 85 88 86
#91 92 83 89 90.5
#
#Sample Output
#90.0
#91.0
#82.0
#90.0
#85.5
#
#Explanation
#Marks obtained by student 1:
#Average marks of student 1:

answerlist = list()
students, marks = map(int,input().split())
for elements in range(marks):
    answerlist.append(list(map(float, input().split())))
answerlist = list(zip(*answerlist))
for lists in answerlist:
    print(sum(lists)/marks)
