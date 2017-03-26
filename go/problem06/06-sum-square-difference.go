package euler

// Answer: 25164150
// Find the difference between the sum of the squares
// of the first one hundred natural numbers and the square of the sum.

// real	0m0.279s
// user	0m0.145s
// sys	0m0.089s
import (
	"fmt"
	"math"
)

func main() {
	a := make(chan int)
	b := make(chan int)
	go func() {
		a <- sumOfSquare(101)
	}()
	go func() {
		b <- squareOfSum(101)
	}()
	fmt.Println(<-b - <-a)
}

func sumOfSquare(n int) int {
	count := 0
	for i := 1; i < n; i++ {
		fmt.Println("at a")
		count += int(math.Pow(float64(i), 2))
	}
	return count
}
func squareOfSum(n int) int {
	count := 0
	for i := 1; i < n; i++ {
		fmt.Println("at b")
		count += i
	}
	return int(math.Pow(float64(count), 2))
}
