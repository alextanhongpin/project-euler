"""
Answer: 443839
"""

def nth_power(n, pow):
  m = sum([ int(str(n)[i]) ** pow
            for i in range(len(str(n)))])
  return m == n


output = filter(lambda x: x is not None and x > 1, [i if nth_power(i, 5)
                                                 else None
                                                 for i in range(10000000)])

print output
total = sum(output)
print total