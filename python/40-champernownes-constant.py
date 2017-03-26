
def main():
    s = "."
    i = 0
    while len(s) < 1000001:
        i += 1
        s += str(i)
    print reduce(lambda a, b: int(a) * int(b), [s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]])

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
