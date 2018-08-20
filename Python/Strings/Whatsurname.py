
#Sample Input
#Guido
#Rossum

#Sample Output
#Hello Guido Rossum! You just delved into python.

def print_full_name(a, b):
    a = "Hello " + str(first_name)
    b = " " + str(last_name) + "! You just delved into python."
    print(a + b)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
