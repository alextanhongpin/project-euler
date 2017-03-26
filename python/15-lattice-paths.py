"""
Lattice paths
Problem 15
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?


Formula: central binomial coefficients

m = (2n)! / (n!)^2

1 x 1 = 2 paths
2 x 2 = 6 paths
3 x 3 = 20 paths
4 x 4 = 70 paths
"""

def central_binomial_coefficient(grid):
    """Calculates the central binomial coefficient"""
    numerator = reduce((lambda x, y: x * y), [n for n in range(2 * grid, 0, -1)])
    denominator = reduce((lambda x, y: x * y), [n for n in range(grid, 0, -1)]) ** 2
    return numerator / denominator

def main():
    """The main application"""
    print('Paths found:', central_binomial_coefficient(20))


if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
