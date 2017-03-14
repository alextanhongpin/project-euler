# Memoiziation

input = 600851475143 
arr = []
prime_numbers = []
for i in range(2, input + 1):
    if input % i is 0:
        possible_division = []
        concat_possible = prime_numbers + [i]
        for j in range(len(concat_possible)):
            if i % concat_possible[j] is 0:
                possible_division.append(concat_possible[j])
        if len(possible_division) is 1:
            arr.append(i)
            prime_numbers.append(i)

print('Max', max(arr), arr)
