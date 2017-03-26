package main

import "testing"

func BenchmarkProblem1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Sum(MultiplesOfThreeAndFive(1000))
	}
}
