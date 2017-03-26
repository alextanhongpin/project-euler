"""
Problem 19 - Counting Sundays
"""
from datetime import date
# Monday is 0,
# Sunday is 6

def main():
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


if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
