import math

def is_unique(n):
    counter = {}
    for i in range(len(str(n))):
        count = counter.get(str(n)[i], 0)
        counter[str(n)[i]] = count + 1
        if counter[str(n)[i]] > 1:
            return False
    return True

def unique_index(n):
    counter = {}
    for i in range(len(str(n))):
        count = counter.get(str(n)[i], 0)
        counter[str(n)[i]] = count + 1
        if counter[str(n)[i]] > 1:
            return i
    return None

def is_pandigital(n):
    return is_unique(n) and "0" not in str(n)



def is_prime (n):
  if n <= 1:
    return False
  elif n == 2:
    return True
  elif n == 3:
    return True
  else:
    square_root = int(math.ceil(math.sqrt(n)))
    for i in range(square_root + 1, 2, -1):
      if n % i == 0:
        return False
      elif n % 2 == 0:
        return False
      elif n % 3 == 0:
        return False
    return True


def round_number(n, i):
    str_n = str(n)
    front = str_n[:i+1]
    back = "0" * len(str_n[i+1:])
    return int(front + back) + 1

def main():
    n = 0
    i = 987654321
    while n == 0:
        i -= 2
        print i
        if is_pandigital(i) and is_prime(i):
            n = i
            print "N found", n
        # else:
        #     index = unique_index(i)
        #     if index is not None:
        #         i = round_number(i, index)
    print n
main()

print is_prime(98765431)