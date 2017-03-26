"""
Problem 21: Amicable numbers
"""

def amicable_number (n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    return count

def main():
    amicable_numbers = set()
    for i in range(1, 10000):
      n = i
      o = amicable_number(n)
      if amicable_number(o) == n and n != o:
        amicable_numbers.add(n)
        amicable_numbers.add(o)
    print "The sum of all amicable numbers under 10000 is:", sum(amicable_numbers)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
