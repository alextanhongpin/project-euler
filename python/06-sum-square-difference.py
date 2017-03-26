"""
Problem 6: Sum square difference
"""

def main():
    """The main application"""
    sum_square = 0
    total = 0
    limit = 100
    for i in range(1, limit + 1):
        sum_square += i ** 2
        total += i
    print total**2 - sum_square

if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
