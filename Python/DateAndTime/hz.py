import calendar
cal = calendar.Calendar()
for x in cal.itermonthdates(2016, 1):
	print(x)
for x in cal.itermonthdays(2016, 1):
	print(x)
#for x in cal.itermonthdays2(2016, 1):
#	print(x)
for x in cal.monthdatescalendar(2016, 1):
	print(x)
for x in cal.monthdays2calendar(2016, 1):
	print(x)
for x in cal.monthdayscalendar(2016, 1):
	print(x)


need to use % and different formatts
#for x in cal.yeardatescalendar(2016, 1):
#	print(x)
#for x in cal.yeardayscalendar(2016, 1):
#	print(x)
#for x in cal.yeardays2calendar(2016, 1):
#	print(x)
