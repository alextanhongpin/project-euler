"""
Lexicographic permutations

Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

def combinations (n, r):
  return math.factorial(n) / math.factorial(r)

arr = [0, 1, 2]
# 0 1 2
# 0 2 1
# 1 0 2
# 1 2 0
# 2 0 1
# 2 1 0


def swap_left (arr):
  out = set()
  total = len(arr)
  count = 0
  for i in range(total):
    for j in range(total):
      if i is not j:
        print i, j
        for k in range(total):
          if j is not k:
            for l in range(total):
              if k is not l:
                for m in range(total):
                  if l is not m:
                    for n in range(total):
                      if m is not n:
                        for o in range(total):
                          if n is not o:
                           for p in range(total):
                            if o is not p:
                              for q  in range(total):
                                if p is not q:
                                  for r  in range(total):
                                    if q is not r:
                                      # if i is not j and i is not k and i is not l and i is not m and i is not n and i is not o and i is not p and i is not q and i is not r:
                                        # out.add("".join([str(i), str(j), str(k), str(l), str(m), str(n), str(o), str(p), str(q)]))
                                      count += 1
                                      # print (count)
                                      if count == 100:
                                        return str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o) + str(p) + str(q) + str(r)


input = ["0","1","2","3", "4", "5", "6", "7", "8", "9"]

o = swap_left(input)

print(o)
print len(o)

# print o[999999]

# print l, len(l), l[999999]

