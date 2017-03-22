import math

def sum_of_factorial(n):
  if len(str(n)) == 1:
    return 0
  total = 0
  for i in range(len(str(n))):
    total += math.factorial(int(str(n)[i]))
  return total

total = 0
for i in range(999999):
  if sum_of_factorial(i) == i:
    total += i

print total

