import math

def is_unique(s):
  c = {}
  for i in range(len(s)):
    count = c.get(s[i], 0)
    c[s[i]] = count + 1
    if c[s[i]] > 1:
      return False
  return True



total = set()

upper = int(math.ceil(math.sqrt(987654321)))
lower = int(math.floor(math.sqrt(123456789)))

start = upper
while start > lower:
  if "0" not in str(start):
    for a in range(start, upper):
      if "0" not in str(a):
        com = str(a)+str(start)+str(a * lower)
        if len(com) == 9 and is_unique(com) and "0" not in com:
            print "MATCHED", com
            total.add(a * b)
  start -= 1
print sum(list(total))
