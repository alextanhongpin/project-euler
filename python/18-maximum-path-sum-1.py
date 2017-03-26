PYRAMID = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# PYRAMID = """3
# 7 4
# 2 4 6
# 8 5 9 3"""
def main():
    """The main application"""
    PARSED = [[int(y) for y in x.split(" ")] for x in PYRAMID.split("\n")]

    y = 0
    total = 0

    arr = []

    theoretical_max = 0
    for i in range(len(PARSED)):
        theoretical_max += max(PARSED[i])

    print theoretical_max
    while y < len(PARSED):
        row = PARSED[y]
        # First row
        if len(row) == 1:
            arr.append(row)
        elif len(row) == 2:
            arr.append(map(lambda x: x + arr[y - 1][0], row))
        else:
            new_arr = []
            for i in range(len(row)):
                if i == 0:
                    new_arr.append(row[i] + arr[y - 1][0])
                elif i == len(row) - 1:
                    new_arr.append(row[i] + arr[y - 1][i - 1])
                else:
                    left = i - 1 if i - 1 > 0 else 0
                    right = i
                    print i, row, arr[y - 1][left:right + 1]
                    new_arr.append(row[i] + max(arr[y - 1][left:right + 1]))
            arr.append(new_arr)
        y += 1

    print "MAX", max(max(arr))


if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
