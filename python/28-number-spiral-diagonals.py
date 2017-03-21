"""
https://projecteuler.net/problem=28
Answer: 669171001
"""
from __future__ import division

grid = 1001
grid_size = grid * grid

tt = 0
for y in range(1, grid + 1, 2):
  for x in range(1, grid_size + 1, 2):
    if x == 1 and y == 1:
      tt += 1
    if x > (y - 2) * (y - 2) and x <= y * y:
      if ((y * y) - x) % (y - 1) == 0:
        print x, y
        tt += x

print tt
# total = 0
# for key in arr:
#   if len(arr[key]) == 1:
#     total += 1
#   else:
#     step = int(len(arr[key]) / 4)
#     for j in range(len(arr[key]) - 1, -1, -step):
#       total += arr[key][j]

# print "Sum of the numbers on the diagonals is:\n", total

