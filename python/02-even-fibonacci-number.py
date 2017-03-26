"""
Problem 2: Even Fibonacci Number
"""

def main():
    """The main application"""
    arr = [1,2]
    output = 0
    while output < 4000000:
        output = arr[len(arr) - 1] + arr[len(arr) - 2]
        arr.append(output)
    print sum(list(filter(lambda x : x % 2 == 0, arr)))

if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
