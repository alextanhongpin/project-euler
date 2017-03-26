package euler

// Answer: 25164150
// Find the difference between the sum of the squares
// of the first one hundred natural numbers and the square of the sum.

// Function that returns a channel
// real  0m0.284s
// user  0m0.151s
// sys 0m0.066s
import (
	"fmt"
	"math"
)

func main() {
	a := sumOfSquare(100)
	b := squareOfSum(100)
	fmt.Println(<-b - <-a)
}

// function that returns a channel
func sumOfSquare(n int) <-chan int {
	c := make(chan int)
	go func() {
		count := 0
		for i := 1; i <= n; i++ {
			count += int(math.Pow(float64(i), 2))
		}
		c <- count
		close(c)
	}()
	return c
}
func squareOfSum(n int) <-chan int {
	c := make(chan int)
	go func() {
		count := 0
		for i := 1; i <= n; i++ {
			count += i
		}
		c <- int(math.Pow(float64(count), 2))
		close(c)
	}()
	return c
}
