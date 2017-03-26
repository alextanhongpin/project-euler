s = """def main():
    output = set()
    for i in range(1000):
        if i % 3 == 0:
            output.add(i)
        if i % 5 == 0:
            output.add(i)
    return sum(output)"""


if __name__ == '__main__':
    print timeit.timeit("problem()", setup="from __main__ import problem")

print timeit.timeit(stmt=s, number=1000)

