#Sample Input
#10
#10

#Sample Output
#45°

import cmath
import math
AB = int(input())
BC = int(input())
number1 = (complex(BC/2,AB/2))
number1 = abs(number1)
number2 = (complex(BC/2,0))
number2 = abs(complex(BC/2,0))
arccos = (math.acos(number2/number1))
deganswer = (math.degrees(arccos))
degreesymbol = (u"\u00b0")
print(str(round(deganswer))+degreesymbol)
degreesymbol = (u"\u00b0")
