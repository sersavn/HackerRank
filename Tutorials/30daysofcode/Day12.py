#Sample Input
#Heraldo Memelli 8135627
#2
#100 80

#Sample Output
#Name: Memelli, Heraldo
#ID: 8135627
#Grade: O

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    def calculate(self):
        a = sum(self.scores)/numScores
        if a >= 90:
            return 'O'
        elif 90 > a >= 80:
            return 'E'
        elif 80 > a >= 70:
            return 'A'
        elif 70 > a >= 55:
            return 'P'
        elif 55 > a >= 40:
            return 'D'
        else:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
