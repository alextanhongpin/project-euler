
def get_last_nth(s, n):
    start = len(s) - n
    end = len(s)
    return s[start:end]


def main():
    i = sum([i ** i for i in range(1, 1001)])
    print get_last_nth(str(i), 10)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
