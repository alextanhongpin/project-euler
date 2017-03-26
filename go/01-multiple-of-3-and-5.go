package main

import "fmt"

// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.
func main() {
	fmt.Println(Sum(MultiplesOfThreeAndFive(1000)))
	// Result should be 1340
}
func MultiplesOfThreeAndFive(number int) []int {
	var multiples []int
	for i := 1; i < number; i++ {
		if i%3 == 0 && i%5 == 0 {
			multiples = append(multiples, i)
		} else if i%5 == 0 {
			multiples = append(multiples, i)
		} else if i%3 == 0 {
			multiples = append(multiples, i)
		}
	}
	return multiples
}
func Sum(multiples []int) int {
	var total int
	for _, v := range multiples {
		total += v
	}
	return total
}
