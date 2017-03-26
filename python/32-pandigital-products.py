import math

def is_unique(s):
    c = {}
    for i in range(len(s)):
      count = c.get(s[i], 0)
      c[s[i]] = count + 1
      if c[s[i]] > 1:
        return False
    return True


def main():
    """The main application"""
    total = set()
    upper = int(math.ceil(math.sqrt(987654321)) / 2) 
    lower = 1

    for a in range(1, upper):
      for b in range(1, upper):
        if "0" not in str(a * b) and is_unique(str(a * b)):
          com = str(a)+str(b)+str(a * b)
          if len(com) == 9 and is_unique(com) and "0" not in com:
              total.add(a * b)

    print sum(list(total))

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
