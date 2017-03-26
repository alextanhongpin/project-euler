import math

def sum_of_factorial(n):
    """Returns the sum of the factorials of a number"""
    if len(str(n)) == 1:
        return 0
    total = 0
    for i in range(len(str(n))):
        total += math.factorial(int(str(n)[i]))
    return total

def main():
    """The main application"""
    total = 0
    for i in range(999999):
        if sum_of_factorial(i) == i:
            total += i
    print total


if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
