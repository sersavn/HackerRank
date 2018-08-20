#Sample Input
#2
#.*\+
#.*+

#Sample Output
#True
#False

#Explanation
#.*\+ : Valid regex.
#.*+: Has the error multiple repeat. Hence, it is invalid.

import re

sampl = 'Aa3 fF8s'

for i in range(int(input())):
    reg = input()
    try:
        check = re.findall(reg, sampl)
        print('True')
    except:
        print('False')

    #print(check)


#line = re.findall('[0-9]+', line)
