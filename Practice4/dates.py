#1
import datetime

today = datetime.datetime.now()
new_date = today - datetime.timedelta(days=5)

print(new_date)

#This program gets the current date and time using datetime.now().
#It subtracts 5 days using datetime.timedelta(days=5).
#Output: current date minus five days.


#2
import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#This program uses date.today() to get the current date.
#It calculates yesterday and tomorrow using timedelta.
#Output: three dates — yesterday, today, tomorrow.


#3
import datetime

now = datetime.datetime.now()
without_microseconds = now.replace(microsecond=0)

print(without_microseconds)

#This program gets the current datetime.
#It removes microseconds using .replace(microsecond=0).
#Output: current datetime without microseconds.


#4
import datetime

date1 = datetime.datetime(2026, 2, 21, 12, 0, 0)
date2 = datetime.datetime(2026, 2, 20, 12, 0, 0)

difference = date1 - date2

print(difference.total_seconds())

#This program creates two datetime objects.
#It subtracts them to get a timedelta object.
#Then it converts the difference to seconds using .total_seconds().
#Output: difference between two dates in seconds.



# The datetime module is used to work with dates and time in Python.
# datetime.now() returns the current date and time.
# A datetime object can also be created by specifying year, month, and day.
# strftime() is used to format a date (for example, getting the year, weekday, or month name).
# Dates can be compared or subtracted to calculate time differences.
