#1
import datetime
x = datetime.datetime.now()
print(x)

#2026-02-21 23:42:03.309990


#2
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#2026
#Saturday


#3
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#2020-05-17 00:00:00


#4
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#June


#5
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y"))

#2026


# The datetime module is used to work with dates and time in Python.
# datetime.now() returns the current date and time.
# A datetime object can also be created by specifying year, month, and day.
# strftime() is used to format a date (for example, getting the year, weekday, or month name).
# Dates can be compared or subtracted to calculate time differences.
