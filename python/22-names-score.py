
alphabets = 'abcdefghijklmnopqrstuvwxyz'

output = 0
with open("./python/22-data.txt") as f:
    lines = [line.split(",") for line in f.readlines()][0]
    lines = map(lambda x: x.replace('"', "").lower(), lines)
    lines.sort()
    for k, v in enumerate(lines):
        total = 0
        for j in range(len(v)):
            total += alphabets.index(v[j]) + 1
        output += total * (k + 1)


print output

