import math

def consequent_numbers(d, n):
  a = n - 1
  b = n
  c = n + 1
  str_d = str(d)
  l = [str_d[a], str_d[b], str_d[c]]
  return int(reduce(lambda x, y: x + y, l))

def divisible_pandigital(n):
  arr = []
  primes = [2, 3, 5, 7, 11, 13, 17]
  for i in range(0, 7):
    c = consequent_numbers(n, i + 2) % primes[i] == 0
    if c == False:
      return False
    arr.append(c)
  if len(filter(lambda x: x, arr)) == 7:
    return True
  return False

def main():
  total = 0
  s = set([0,1,2,3,4,5,6,7,8,9])
  for a in range(len(s)):
    if list(s)[a] == 0:
      s = set([0,1,2,3,4,5,6,7,8,9])
      continue
    else:
      s.remove(a)
    print a, s
  print total

# main()
def loop(i, n, f=""):
  f += str(i)
  n.remove(i)
  if len(n) > 0:
    return loop(i, n, f)
  else:
    return f

print loop(3, set([0,1,2,3,4,5,6,7,8,9]), "")