"""
Answer: 443839
"""

def nth_power(n, pow):
  m = sum([ int(str(n)[i]) ** pow
            for i in range(len(str(n)))])
  return m == n


def main():
    """The main application"""
    output = filter(lambda x: x is not None and x > 1, [i if nth_power(i, 5)
                                                     else None
                                                     for i in range(10000000)])

    total = sum(output)
    # print total

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
