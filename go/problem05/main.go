package main

import "fmt"

// Answer: 232792560
func main() {
	i := smallestMultiple(20 * 19 * 1000)
	fmt.Println(i)
}

func smallestMultiple(val int) int {
	for isDivisible(val, 20) == false {
		val += 20 * 19
	}
	return val
}

func isDivisible(n, r int) bool {
	for i := 1; i <= r; i++ {
		if n%i != 0 {
			return false
		}
	}
	return true
}
