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

def main():
    with open('./42-data.txt') as f:
      lines = f.readlines()[0].replace('"', '').split(',')
      output = [compute_triangle_number(x) for x in lines]
      print len(filter(lambda x: x, output))


if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
