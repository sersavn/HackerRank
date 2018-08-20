#Sample Input
#08 05 2015

#Sample Output
#WEDNESDAY

import calendar
month, day, year = map(int, input().split())
thedayis = calendar.weekday(year, month, day)
answer = calendar.day_name[thedayis]
print(answer.upper())
