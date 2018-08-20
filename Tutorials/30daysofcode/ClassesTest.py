class Simple:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Summa(Simple):
    def calculate(self):
        doesntmatter = a + 3*b
        return doesntmatter

line = input().split()
a = line[0]
b = line[1]
s = Summa(a,b)
print(s.calculate())
