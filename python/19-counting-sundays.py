"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date

# Monday is 0,
# Sunday is 6

start = date(1901, 1, 1)
end = date(2000, 12, 31)
number_of_months = (end.year - start.year + 1) * 12

is_sunday = 0
start_year = 1901
for month in range(number_of_months):
  current_month = (month + 1) % 12
  if date(start_year, 12 if current_month is 0 else current_month, 1).weekday() == 6:
    print date(start_year, 12 if current_month is 0 else current_month, 1)
    is_sunday += 1
  if current_month == 0:
    start_year += 1

print "The number of sundays that fell for the first of the month is:", is_sunday