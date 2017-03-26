import math

def is_pentagonal_number(n):
    np = (1 + math.sqrt(1 + 24 * n)) / 6
    if int(np) == np:
        return True
    return False

def is_hexagonal_number(n):
    np = (1 + math.sqrt(1 + 8 * n)) / 4
    if int(np) == np:
        return True
    return False

def triangle_number(n):
    return n * (n + 1) / 2


def main():
    s = set()
    i = 1
    while len(s) < 2:
        i += 1
        print i
        t = triangle_number(i)
        if is_hexagonal_number(t) and is_pentagonal_number(t):
            s.add(t)
    print s

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
