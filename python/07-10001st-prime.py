'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?'''

from prime import is_prime 

def main():
    """The main application"""
    start = 2
    arr = []

    while len(arr) < 10001:
        if is_prime(start):
            arr.append(start)
        start += 1

    # print("The 10,001st prime number is:", arr[-1])

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
