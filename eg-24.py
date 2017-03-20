
print "hello"
def is_unique_str (input):
    print "input", input
    counter = {}
    for i in range(len(input)):
        count = counter.get(input[i], 0)
        counter[input[i]] = count + 1
        if counter[input[i]] > 1:
            return False
    return True

count = 0
for i in range(123456789, 9876543210):
    if is_unique_str(str(i)):
        count += 1
        print count
        if count == 1000000:
            print i
            break