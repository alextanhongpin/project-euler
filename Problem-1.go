package main

import "fmt"

// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.
func main() {
	var multiples []int
	var max int

	// Let max be 1000
	max = 1000
	for i := 1; i < max; i++ {
		if max%i == 0 {
			multiples = append(multiples, i)
		}
	}
	sum := 0
	for v := range multiples {
		sum += multiples[v]
	}
	fmt.Println(sum)
	// Result should be 1340
}
