from __future__ import division


def is_unique (n):
    counter = {}
    for i in range(len(n)):
        count = counter.get(n[i], 0)
        counter[n[i]] = count + 1
        if counter[n[i]] > 1:
            return False
    return True

def is_same(n):
    for i in range(len(n)):
        if n[0] != n[i]:
            return False
    return True


def get_repeating (n):
    out = str(n).split(".")[1]
    half = int(len(out) / 2)
    print out
    if is_unique(out):
        return out
    elif is_same(out):
        return out[0]
    return out[0:half]



max = -9999
max_int = 0
for i in range(1000):
    try:
        length = len(get_repeating(1 / i))
        print get_repeating(1 / i)
        if length > max:
            max = length
            max_int = i
    except ZeroDivisionError:
        print "i"

print max_int, max