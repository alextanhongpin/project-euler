package main

import "fmt"

// Answer: 232792560
func main() {
	i := 20 * 19 * 1000
	for isDivisible(i, 20) == false {
		i += 20 * 19
		fmt.Println(i)
	}
	fmt.Println(i)
}

func isDivisible(n, r int) bool {
	for i := 1; i <= r; i++ {
		if n%i != 0 {
			return false
		}
	}
	return true
}
