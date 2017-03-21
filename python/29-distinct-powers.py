"""
Answer: 9183
"""

def distinct_powers (a, b):
  return a ** b

s = set()
for i in range(2, 101):
  for j in range(2, 101):
    print distinct_powers(i, j)
    s.add(distinct_powers(i, j))

print s, len(s)