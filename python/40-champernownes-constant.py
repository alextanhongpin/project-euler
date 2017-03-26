
def main():
    s = "."
    i = 0
    while len(s) < 1000001:
        i += 1
        s += str(i)
    print [s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]]
    print reduce(lambda a, b: int(a) * int(b), [s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]])

main()