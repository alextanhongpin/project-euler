import math

def pentagon_numbers(n):
  return n * (3 * n - 1) / 2

def is_pentagonal(c):
  s = (1 + math.sqrt(1 - (24 * -c))) / 6
  if int(s) != s:
    return False
  return True

c = 0
d = {}
upper = 2170

while c < upper:
  d[c] = pentagon_numbers(c)
  c += 1

out = 0
is_solved = False
i = 0
while is_solved is False:
  for j in range(1, i - 1):
    if i < j:
      continue
    a = d.get(i, 0)
    b = d.get(j, 0)
    n = is_pentagonal(a + b)
    m = is_pentagonal(a - b)
    if n and m:
      out = a - b
      print "out", out
      is_solved = True
  i += 1
print out


# 95, 28, 99
# 97, 52, 110
# 99, 32, 104
