package main

import "testing"

// go test -bench=. ./test

func BenchmarkProblem05(b *testing.B) {
	for i := 0; i < b.N; i++ {
		smallestMultiple(20 * 19 * 1000)
	}
}
