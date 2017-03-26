import math

from prime import is_prime
def is_unique(n):
    counter = {}
    for i in range(len(str(n))):
        count = counter.get(str(n)[i], 0)
        counter[str(n)[i]] = count + 1
        if counter[str(n)[i]] > 1:
            return False
    return True

def unique_index(n):
    counter = {}
    for i in range(len(str(n))):
        count = counter.get(str(n)[i], 0)
        counter[str(n)[i]] = count + 1
        if counter[str(n)[i]] > 1:
            return i
    return None

def is_pandigital(n):
    return is_unique(n) and "0" not in str(n)


def round_number(n, i):
    str_n = str(n)
    front = str_n[:i+1]
    back = "0" * len(str_n[i+1:])
    return int(front + back) + 1

def main():
    n = 0
    i = 987654321
    while n == 0:
        i -= 2
        if is_pandigital(i) and is_prime(i):
            n = i
        # else:
        #     index = unique_index(i)
        #     if index is not None:
        #         i = round_number(i, index)
    print n

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)



