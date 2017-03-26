"""Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prime import is_prime

def main():
    prime = 2
    count = 0
    total = 0
    limit = 2000000
    while prime < limit:
        if is_prime(count):
            prime = count
        if prime < limit:
            total += prime
        else:
            break
        count += 1

    print("The total of prime below 2 million is:", total)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
