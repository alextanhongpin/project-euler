"""
App
Sub-string divisibility
"""
import math
import random

def consequent_numbers(d, n):
    """
    """
    a = n - 1
    b = n 
    c = n + 1
    str_d = str(d)
    l = [str_d[a], str_d[b], str_d[c]]
    return int(reduce(lambda x, y: x + y, l))

def divisible_pandigital(n):
    """
    """
    if len(str(n)) < 10:
        return False
    arr = []
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(0, 7):
        c = consequent_numbers(n, i + 2) % primes[i] == 0
        if c == False:
            return False
        arr.append(c)
        if len(filter(lambda x: x, arr)) == 7:
            return True
    return False



def main():
    """
        The main app
    """
    original = [0,1,2,3,4,5,6,7,8,9]
    data = original[:]
    out = ""
    new_set = set()
    LEN = len(data)
    while len(new_set) < math.factorial(LEN):
        print len(new_set), math.factorial(LEN)
        if len(data) > 0:
            index = random.randint(0, len(data) - 1)
            cut = data.pop(index)
            out += str(cut)
        if len(out) == LEN:
            new_set.add(int(out))
            out = ''
            data = original[:]
    print new_set, len(new_set)
    print sum([int(x) if divisible_pandigital(x) else 0 for x in new_set])

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)


