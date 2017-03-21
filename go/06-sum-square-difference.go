package main

// Answer: 25164150

import (
	"fmt"
	"math"
)

func main() {
	sum := 0
	sumOfSquare := 0
	for i := 1; i < 101; i++ {
		sum += i
		sumOfSquare += int(math.Pow(float64(i), 2))
	}
	squareOfSum := int(math.Pow(float64(sum), 2))
	difference := squareOfSum - sumOfSquare
	fmt.Println(difference)
}
