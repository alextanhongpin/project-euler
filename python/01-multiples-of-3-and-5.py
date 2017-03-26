

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

print "Average for 10 times:{0}".format(sum(out) / len(out))


import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

with Timer() as t:
    main()
print  "=> elasped lpush: %s s" % t.secs