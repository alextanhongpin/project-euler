# def to_binary(power):
#   return lambda x: int(bin(x)[:1:-1], power)
# power10 = to_binary(10)

def is_palindrome(n):
  return str(n)[::-1] == str(n)

def to_binary(n):
  return "{0:b}".format(n)

def main():
    """The main application"""
    upper = 1000000
    count = 0
    for i in range(upper):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            count += i
    print "Answer:", count


if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
