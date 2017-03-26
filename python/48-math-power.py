
def get_last_nth(s, n):
    start = len(s) - n
    end = len(s)
    return s[start:end]


i = sum([i ** i for i in range(1, 1001)])
print get_last_nth(str(i), 10)