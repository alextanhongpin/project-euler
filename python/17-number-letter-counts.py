"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def main():
    """The main application"""
    all = []
    less_than_ten = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    twenty_to_ninety = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


    all += less_than_ten + ten_to_nineteen + twenty_to_ninety
    for i in range(len(twenty_to_ninety)):
      for j in range(len(less_than_ten)):
        all += [twenty_to_ninety[i] + ' ' + less_than_ten[j]]

    print all
    hundred_to_nine_hundred = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

    all += hundred_to_nine_hundred

    for i in range(len(hundred_to_nine_hundred)):
      for j in range(len(twenty_to_ninety)):
        all += [hundred_to_nine_hundred[i] + ' and ' + twenty_to_ninety[j]]
        for k in range(len(less_than_ten)):
          all += [hundred_to_nine_hundred[i] + ' and ' + twenty_to_ninety[j] + less_than_ten[k]]
      for l in range(len(ten_to_nineteen)):
        all += [hundred_to_nine_hundred[i] + ' and ' + ten_to_nineteen[l]]
      for m in range(len(less_than_ten)):
        all += [hundred_to_nine_hundred[i] + ' and ' + less_than_ten[k]]
    thousand = ["one thousand"]
    all += thousand

    for i in range(len(all)):
      print all[i] 

    print len(all)
    def join_str(a, b):
      return a + b
    output = reduce(join_str, [ reduce(join_str, x.split())
                for x in all])
    print len(output)

if __name__ == '__main__':
    import timeit
    ITERATIONS = 100
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
