"""
Problem 22: The names score
"""

def main():
    """The main application"""
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    output = 0
    with open("./22-data.txt") as file_content:
        lines = [line.split(",") for line in file_content.readlines()][0]
        lines = [x.replace('"', "").lower() for x in lines]
        lines.sort()
        for key, value in enumerate(lines):
            total = 0
            for _, j in enumerate(value):
                total += alphabets.index(j) + 1
            output += total * (key + 1)


    print output

if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
