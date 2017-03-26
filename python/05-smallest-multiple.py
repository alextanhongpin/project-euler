"""
Problem 5: Smallest multiple
"""
def smallest_multiple(count, limit):
    """Get the smallest multiple"""
    for i in range(limit, 1, -1):
        if count % i != 0:
            return False
    return True

def main():
    """The main application"""
    i = 20 * 19 * 1000
    while smallest_multiple(i, 20) is False:
        i += 20 * 19
    print i


if __name__ == '__main__':
    import timeit
    ITERATIONS = 50
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
