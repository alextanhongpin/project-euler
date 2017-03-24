import math
def is_triangle_number(n, o):
  return int(0.5 * n * (n + 1)) == o

def alphabet_index(a):
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  return alphabets.find(a) + 1


def compute_triangle_number(s):
  count = 0
  for i in range(len(s)):
    index = s[i].lower()
    count += alphabet_index(index)
  upper = int(math.ceil(math.sqrt(count * 2)))
  lower = 0 
  for i in range(upper, lower, -1):
    if is_triangle_number(i, count):
      print s
      return True
  return False


with open('./python/42-data.txt') as f:
  lines = f.readlines()[0].replace('"', '').split(',')
  output = [compute_triangle_number(x) for x in lines]
  print len(filter(lambda x: x, output))

