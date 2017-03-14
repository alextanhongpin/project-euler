from timeit import default_timer as timer
def smallest_multiple (n, m):
    for i in range(m, 1, -1):
        if n % i != 0:
            return False
    return True

i = 20 * 19 * 1000
start = timer()
while smallest_multiple(i, 20) is False:
    print("Index:", i)
    i += 20 * 19
end = timer()

print(i)
print("Time:", end - start)
