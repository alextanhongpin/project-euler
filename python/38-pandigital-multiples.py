import math

def is_within_range(n):
  if "0" in n:
    return False
  if len(n) != 9:
    return False
  return True

def is_unique(n):
  counter = {}
  for i in range(len(n)):
    count = counter.get(n[i], 0)
    counter[n[i]] = count + 1
    if counter[n[i]] > 1:
      return False
  return True



def main():
  s = ""
  output = 0
  upper = int(math.ceil(math.sqrt(987654321)))
  for i in range(1, upper):
    s = ""
    for j in range(1, 9):
      s += str(i * j)
      if is_unique(s) and is_within_range(s):
        if int(s) > output:
          output = int(s)
  print output
main()