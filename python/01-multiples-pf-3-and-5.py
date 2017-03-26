"""
Problem 1: Multiples of 3 and 5
"""

def main():
    """The main application"""
    output = []
    for i in range(1000):
        if i % 3 == 0 and i % 5 == 0:
            output.append(i)
        elif i % 3 == 0:
            output.append(i)
        elif i % 5 == 0:
            output.append(i)
    return sum(output)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
