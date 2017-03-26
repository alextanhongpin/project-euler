"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n > n/2 (n is even)
n > 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def handle_even(number):
    """Handle if a number is even"""
    return number / 2

def handle_odd(number):
    """Handle if a number is odd"""
    return 3 * number + 1

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def chain_length(number):
    """Get the length of the chain"""
    count = 1
    while number != 1:
        count += 1
        if is_even(number):
            number = handle_even(number)
        else:
            number = handle_odd(number)
    return count

def main():
    """The main application"""
    arr = []
    for i in range(1000000, 1, -1):
        arr.append(chain_length(i))
    print "The longest chain is: {}".format(arr.index(max(arr)))

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
