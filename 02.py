# Memoiziation

input = 600851475143 
arr = []
prime_numbers = [5, 7, 13, 29]
for i in range(2, input + 1):
    if input % i is 0:
        possible_division = []
        for j in range(len(prime_numbers)):
            if i % prime_numbers[j] is 0:
                possible_division.append(prime_numbers[j])
        if len(possible_division) is 1:
            arr.append(i)
            prime_numbers.append(i)

print('Max', max(arr), arr)
