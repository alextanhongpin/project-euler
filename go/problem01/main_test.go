package main

import "testing"

// go test -bench=. ./test

func BenchmarkProblem01(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Sum(MultiplesOfThreeAndFive(1000))
	}
}
