
import math

def perimeter(a, b, c, output):
  return a + b + c == output

def is_right_angled_triangle(a, b, c):
  if a is 0 or b is 0 or c is 0:
    return False
  return a ** 2 + b ** 2 - c ** 2 == 0

def pythogaras(a, b):
  return math.sqrt(a ** 2 + b ** 2)

upper = 500
defined_perimeter = 0
output = 0
while defined_perimeter <= 1000:
  s = []
  print defined_perimeter
  for a in range(1, upper):
    for b in range(1, upper):
      if a + b < defined_perimeter:
        c = int(pythogaras(a, b))
        if is_right_angled_triangle(a, b, c) == False:
          continue
        if perimeter(a, b, c, defined_perimeter):
          out = [str(a), str(b), str(c)]
          out.sort()
          s.append(",".join(out))
  if len(s) > output:
    output = len(s)
  defined_perimeter += 1

print "Answer:", output
