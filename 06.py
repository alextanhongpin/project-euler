sum_square = 0
sum = 0
for i in range(1, 101):
  sum_square += i ** 2
  sum += i

print(sum**2 - sum_square)