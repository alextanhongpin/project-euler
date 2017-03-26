

def main():
    """
    The main application
    """
    output = set()
    for i in range(1000):
        if i % 3 == 0:
            output.add(i)
        if i % 5 == 0:
            output.add(i)
    return sum(output)

def benchmark(fn):
    """
    Benchmark the results
    """
    from timeit import default_timer as timer
    start = timer()
    output = fn()
    print output
    end = timer()
    diff = end - start
    print "The function takes {0} ms to complete".format(diff)
    return diff

out = []
for i in range(10):
    out.append(benchmark(main))

print sum(out) / len(out)