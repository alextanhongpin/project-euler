"""
Answer: 9183
"""

def distinct_powers (a, b):
  return a ** b

def main():
    """The main application"""
    s = set()
    for i in range(2, 101):
      for j in range(2, 101):
        s.add(distinct_powers(i, j))
    # print s, len(s)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
